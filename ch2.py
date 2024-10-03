import cv2
import numpy
import numpy as np
import os

#img = np.zeros((3,3), dtype=np.uint8)
#img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#print(img)

#print(img.shape)

image = cv2.imread('/home/james/Downloads/jamie_and_izzy.jpg')
image[:,:,0] = 0
cv2.imshow('test',image)
cv2.waitKey()
cv2.destroyAllWindows()
#cv2.imwrite('jai_no_green.jpg', image)


randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

# convert into 400x300 grayscale image
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png', grayImage)

# convert into 400x100 color image
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png', bgrImage)
