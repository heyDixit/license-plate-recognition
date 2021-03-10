from cv2 import cv2
import imutils 
import pytesseract

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Reading the image file

image = cv2.imread("1.jpg") 
image=imutils.resize(image, width=500)
cv2.imshow("Orignal Image", image)
cv2.waitKey(0) 


# Image Conversion to grayscale

gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image", gray)
cv2.waitKey(0)
