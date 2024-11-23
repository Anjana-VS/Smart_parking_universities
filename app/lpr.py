import cv2
import pytesseract

def recognize_plate(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plate = pytesseract.image_to_string(gray, config='--psm 8')
    return plate.strip()
