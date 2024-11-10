package com.example.markdetail

import android.annotation.SuppressLint
import android.database.Cursor
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.MediaStore
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar
import androidx.documentfile.provider.DocumentFile
import kotlinx.coroutines.CoroutineStart
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.MultipartBody
import okhttp3.RequestBody
import okhttp3.ResponseBody
import org.json.JSONObject
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Multipart
import retrofit2.http.Part
import retrofit2.http.POST
import java.io.File

import android.util.Base64
import org.json.JSONException
import kotlin.io.encoding.ExperimentalEncodingApi

@Suppress("DEPRECATION")
class ImagePreviewActivity : AppCompatActivity() {

    private lateinit var imageView: ImageView
    private lateinit var textview: TextView
    private lateinit var uploadButton: Button
    private var imageUri: Uri? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_preview)

        val toolbar: Toolbar = findViewById(R.id.toolbar)
        setSupportActionBar(toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = "Image Preview"

        imageView = findViewById(R.id.image_view)
        textview = findViewById(R.id.textView2)
        uploadButton = findViewById(R.id.upload_button)

        imageUri = intent.getParcelableExtra("imageUri")

        imageView.setImageURI(imageUri)

        uploadButton.setOnClickListener {
            imageUri?.let { uri -> uploadImage(uri) }
        }
    }
    data class ApiResponse(
        val status: String,
        val filename: String,
        val text_data: String,
        val img: String
    )
    private fun uploadImage(imageUri: Uri) {
        val inputStream = contentResolver.openInputStream(imageUri)
        if (inputStream != null) {

            val requestFile = RequestBody.create("image/jpeg".toMediaType(), inputStream.readBytes())
            val body = MultipartBody.Part.createFormData("image", "image.jpg", requestFile)

            val retrofit = Retrofit.Builder()
                .baseUrl("http://192.168.0.4:9871/")
                .addConverterFactory(GsonConverterFactory.create())
                .build()

            val apiService = retrofit.create(ApiService::class.java)
            apiService.uploadImage(body).enqueue(object : Callback<ResponseBody> {
                override fun onResponse(call: Call<ResponseBody>, response: Response<ResponseBody>) {
                    if (response.isSuccessful) {
                        val responseBody = response.body()

                        if (responseBody != null) {
                            try {
                                val jsonResponse = responseBody.string()
                                val jsonObject = JSONObject(jsonResponse)
                                val base64Image = jsonObject.optString("img", "")
                                val textData = jsonObject.optString("text_data", "No text data available")
                                if (base64Image.isNotEmpty()) {
                                    val decodedBytes = Base64.decode(base64Image, Base64.DEFAULT)

                                    val decodedImage = BitmapFactory.decodeByteArray(decodedBytes, 0, decodedBytes.size)

                                    imageView.setImageBitmap(decodedImage)
                                } else {
                                    Toast.makeText(this@ImagePreviewActivity, "No image data available", Toast.LENGTH_SHORT).show()
                                }

                                textview.text = textData


                            } catch (e: Exception) {
                                e.printStackTrace()
                                Toast.makeText(this@ImagePreviewActivity, "Error processing image", Toast.LENGTH_SHORT).show()
                            }
                        }
                    } else {
                        Toast.makeText(this@ImagePreviewActivity, "Upload failed", Toast.LENGTH_SHORT).show()
                    }
                }

                override fun onFailure(call: Call<ResponseBody>, t: Throwable) {
                    Toast.makeText(this@ImagePreviewActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
                }
            })
        } else {
            Toast.makeText(this, "Failed to open image", Toast.LENGTH_SHORT).show()
        }
    }

    private fun getRealPathFromURI(contentUri: Uri): String {
        var path = ""

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            val documentFile = DocumentFile.fromSingleUri(this, contentUri)
            documentFile?.let {
                path = it.uri.path ?: ""
            }
        } else {
            val cursor: Cursor? = contentResolver.query(contentUri, null, null, null, null)
            cursor?.use {
                if (it.moveToFirst()) {
                    val columnIndex = it.getColumnIndex(MediaStore.Images.Media.DATA)
                    if (columnIndex != -1) {
                        path = it.getString(columnIndex)
                    }
                }
            }
        }

        return path
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressed()
        return true
    }

    interface ApiService {
        @Multipart
        @POST("api/upload")
        fun uploadImage(@Part image: MultipartBody.Part): Call<ResponseBody>
    }
}