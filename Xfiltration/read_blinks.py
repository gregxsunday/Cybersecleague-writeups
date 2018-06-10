import cv2
import numpy

vidcap = cv2.VideoCapture('router.mp4')
success,image = vidcap.read()

count = 0
success = True
res = ''

while success:
    success,frame = vidcap.read()
    pix = numpy.array(frame)
    if success:
        pixel = pix[418,680]
        if pixel[1] > 100:
            res += '1'
        else:
            res += '0'
        count += 1

print('%d frames = %d seconds' % (count, count // 15))

with open('led.txt', 'w') as f:
    f.write(res)
