def recognize_digits_ocr(image, reader):
    ocr_result = reader.recognize(image)
    digits = list(str(ocr_result[0][-2]))

    return digits