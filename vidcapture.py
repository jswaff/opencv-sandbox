import cv2
import numpy
import numpy as np
import os


videoCapture = cv2.VideoCapture('/home/james/data/20220824_094923_gray.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
print('fps=', fps)

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'test.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()

