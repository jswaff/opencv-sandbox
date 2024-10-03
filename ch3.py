import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])

kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                       [-1,1,2,1,-1],
                       [-1,2,4,2,-1],
                       [-1,1,2,1,-1],
                       [-1,-1,-1,-1,-1]])

img = cv2.imread('/home/james/Downloads/jamie_and_izzy.jpg', 0)

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv2.GaussianBlur(img, (17,17), 0)
g_hpf = img - blurred

# cv2.imshow("3x3", k3)
# cv2.imshow("5x5", k5)
# cv2.imshow("blurred", blurred)
# cv2.imshow("g_hpf", g_hpf)
# cv2.waitKey()
# cv2.destroyAllWindows()

# image = cv2.imread('/home/james/Downloads/jamie_and_izzy.jpg')
# cv2.imwrite('canny.png', cv2.Canny(img, 200, 300))
# cv2.imshow('canny',cv2.imread('canny.png'))
# cv2.waitKey()
# cv2.destroyAllWindows()


# img = np.zeros((200,200),dtype=np.uint8)
# img[50:150, 50:150] = 255
#
# ret, thresh = cv2.threshold(img, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
#                                        cv2.CHAIN_APPROX_SIMPLE)
# color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
# cv2.imshow("contours", color)
# cv2.waitKey()
# cv2.destroyAllWindows()

# img = cv2.pyrDown(cv2.imread('/home/james/Downloads/jamie_and_izzy.jpg', cv2.IMREAD_UNCHANGED))
#
# ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
# contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# for c in contours:
#     # find bounding box coordinates
#     x,y,w,h = cv2.boundingRect(c)
#     cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),2)
#
#     # find minimum area
#     rect = cv2.minAreaRect(c)
#     # calculate coordinates of the minimum area rectangle
#     box = cv2.boxPoints(rect)
#     # normalize coordinates to integers
#     box = np.int0(box)
#     # draw contours
#     cv2.drawContours(img, [box], 0, (0,0,255), 3)
#
#     # calculate center and radius of minimum enclosing circle
#     (x,y), radius = cv2.minEnclosingCircle(c)
#     # cast to integers
#     center = (int(x),int(y))
#     radius = int(radius)
#     # draw the circle
#     img = cv2.circle(img, center, radius, (0,255,0), 2)
#     cv2.drawContours(img, contours, -1, (255,0,0), 1)
#
# cv2.imshow('contours', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


#########
img = cv2.imread('/home/james/Downloads/jamie_and_izzy.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
minLineLength = 20
maxLineGap = 5
lines = cv2.HoughLinesP(edges, 1, np.pi/180.0, 20, minLineLength, maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img, (x1,y1),(x2,y2),(0,255), 2)

cv2.imshow('edges', edges)
cv2.imshow('lines', img)
cv2.waitKey()
cv2.destroyAllWindows()

