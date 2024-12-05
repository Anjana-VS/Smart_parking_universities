import pytesseract
import cv2
from PIL import Image

def detect_license_plate(img_path):
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

    plates = plate_cascade.detectMultiScale(gray, 1.1, 10)
    for (x, y, w, h) in plates:
        plate_region = image[y:y + h, x:x + w]
        pil_img = Image.fromarray(plate_region)
        license_plate = pytesseract.image_to_string(pil_img)
        return license_plate
    return None
