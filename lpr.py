from cv2 import cv2
import imutils # to resize our image
import pytesseract

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#now to read the image file
image = cv2.imread("1.png")
#we will resize and standardize our image to 500
image=imutils.resize(image, width=500)
#we will display orignal image when it will start finding
cv2.imshow("Orignal Image", image) #here orignal image is the name of window /// you can give your suitable name
cv2.waitKey(0) #till i press anything it will not execute further