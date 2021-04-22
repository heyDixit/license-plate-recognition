from cv2 import cv2
import imutils 
import pytesseract

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Reading the image file

image = cv2.imread("1.jpg") 
image=imutils.resize(image, width=500)
cv2.imshow("Orignal Image", image)



# Image Conversion to grayscale

gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image", gray)
cv2.waitKey(0)

#now we will reduce noise from the image and make it smooth

gray = cv2.bilateralFilter(gray, 11 , 17 , 17)
cv2.imshow("Smoother Image", gray)
cv2.waitKey(0)

#so now we will find the edges of the images
edged = cv2.Canny(gray, 170 , 200)
cv2.imshow("Canny edge", edged)
cv2.waitKey(0)

# Find the contours based on the images
cntns , new = cv2.findContours(edged.copy() , cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)


# Copy orignal image to draw all the contours
image1 = image.copy()
cv2.drawContours(image1 , cntns , -1 , (0,255,0), 3) # this values are fixed to draw all the contours in an image
cv2.imshow("Canny after contouring", image1)
cv2.waitKey(0)

# Reverse the order of sorting

