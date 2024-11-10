import cv2

def draw_bbox_on_image(image, bbox):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        x, y, w, h = bbox
        cv2.rectangle(image_rgb, (x-w//2, y-h//2), (x+w//2, y+h//2), (255, 0, 0), 4)
        return image_rgb

def crop_image(image_path, bbox):
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        x, y, w, h = bbox
        cropped_part = image_rgb[y-h//2:y+h//2, x-w//2:x+w//2]
        return cropped_part