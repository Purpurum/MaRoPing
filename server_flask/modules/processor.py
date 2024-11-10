import cv2
from rapidfuzz import process
from detectors import detect
from recognizers import recognize_digits_ocr
from util_functions import crop_image, draw_bbox_on_image

def process_image(image, detector_code, detector_art, reader, articules):
    #Детекция артикула
    art_detection_res = detect(image, detector_art)
    if art_detection_res["x"] != 0 and art_detection_res["y"] != 0 and art_detection_res["w"] != 0 and art_detection_res["h"] != 0:
        image_art = crop_image(image, [art_detection_res["x"], art_detection_res["y"], art_detection_res["w"], art_detection_res["h"]])
        bbox_art = [art_detection_res["x"], art_detection_res["y"], art_detection_res["w"], art_detection_res["h"]]
    else:
        image_art = None
        bbox_art = [0,0,0,0]
    #Детекция кода
    code_detection_res = detect(image, detector_code)
    if code_detection_res["x"] != 0 and code_detection_res["y"] != 0 and code_detection_res["w"] != 0 and code_detection_res["h"] != 0:
        image_code = crop_image(image, [code_detection_res["x"], code_detection_res["y"], code_detection_res["w"], code_detection_res["h"]])
        bbox_code = [code_detection_res["x"], code_detection_res["y"], code_detection_res["w"], code_detection_res["h"]]
    else:
        image_code = None
        bbox_code = [0,0,0,0]

    #Распознавание артикула
    if image_art is not None:
        art_recognition_res = recognize_digits_ocr(image_art, reader)
    else:
        art_recognition_res = ""
    
    #Распознавание кода
    if image_code is not None:
        code_recognition_res = recognize_digits_ocr(image_code, reader)
    else:
        code_recognition_res = ""

    #получение артикула из базы
    if art_recognition_res != "":
        search_results_art = process.extractOne("".join(art_recognition_res), articules, score_cutoff=10)
    else:
        search_results_art = ""
    
    if search_results_art != "":
        art = search_results_art[0].replace('"', '')
    else:
        art = ""
    
    #Формирование текста для вывода
    label_text = f'{art} {"".join(code_recognition_res)}'

    #Формирование изображения для вывода
    image_clean = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)
    image_art = draw_bbox_on_image(image_clean, bbox_art)
    image_art_code = draw_bbox_on_image(image_art, bbox_code)

    return label_text, image_art_code
    



