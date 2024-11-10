<div align="center">
  <img src="https://i.ibb.co/XbjrQZ4/qx-KFQHTELBc.jpg" alt="banner2" border="0" /></a>
</div>

## <div align="center">Стэк технологий📑</div>
<div align="center">
  <a href="https://www.python.org/doc/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
  <a href="https://pytorch.org/docs/stable/index.html"><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white"></a>
  <a href="https://opencv.github.io/cvat/docs/"><img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"></a>
  <a href="https://github.com/JetBrains/kotlin"><img src="https://img.shields.io/badge/kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white"></a>
  <a href="https://developer.android.com/develop"><img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white"></a>
  <a href="https://flask.palletsprojects.com/en/stable/"><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"></a>
  <a href="https://httpd.apache.org/"><img src="https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white"></a>

  <br>
  <a href="https://github.com/ultralytics/ultralytics?tab=readme-ov-file"><img src="https://img.shields.io/badge/Ultralytics-YOLOv11-purple.svg"></a>
</div>

## <div align="center">О решении📝</div>
<p align="justify">Мы рады представить наше приложение, построенное на клиент-серверной архитектуре. Наше решение включает программный модуль, способный автоматически распознавать маркировку деталей по фотографиям, сделанным на различных металлических поверхностях.
</p>

## <div align="center">Описание решения🧰</div>

<p align="justify">
Данное решение представляет собой мобильное приложение, разработанное для платформы Android, которое взаимодействует с серверной частью, реализованной с использованием Flask и размещенной на сервере Apache.
</p>

### Архитектура

<p align="justify">
<ul> 
<li>Клиентская часть (Android-приложение):</li>
  <ul>
  <li>Язык программирования: Java/Kotlin;</li>
  <li>Интерфейс пользователя: Разработан с использованием Android SDK;</li>
  <li>Взаимодействие с сервером: Использует HTTP-запросы для обмена данными с серверной частью. Для этого используется библиотека <a href="https://square.github.io/retrofit/">Retrofit</a>.</li>
  </ul>
<li>Серверная часть (Flask):</li>
  <ul>
  <li>Язык программирования: Python;</li>
  <li>Фреймворк: Flask — легковесный веб-фреймворк;</li>
  <li>Сервер: Apache — используется для развертывания приложения и обработки входящих HTTP-запросов;</li>
  </ul>
<li>Нейронный программный модуль:</li>
  <ul>
  <li>YOLOv11: Модель для детекции объектов, используемая для определения кода и артикула на изображениях.</li>
  <li>EasyOCR: Библиотека для оптического распознавания текста (OCR), которая используется для считывания кода и артикула после их детекции.</li>
  </ul> 
</ul>
</p>

## <div align="center">Программный модуль 🔮</div>

<p align="justify">
  
####  Основная логика нейронного модуля находится в файле <a href="ССЫЛКА">FULL_LAUNCH.ipynb</a>. Можно протестировать качество работы моделей.
</p>
<p>
Для запуска необходим Python 3.10.0 и следующие библиотеки:
</p>
  
```bash
$ pip install ultralytics
$ pip install numpy
$ pip install opencv-python
$ pip install easyocr
$ pip install pandas
$ pip install matplotlib
```

### Как это работает?
<p>
  ТУДУ (Описать работу програмного модуля)
</p> 
 
</details>

## <div align="center">Пример работы программного модуля📸</div>
<p>
  <br>
</p>
<div align="center">
  <!--<img src="" width="500" height="500"/>-->

</div>

