import numpy as np
import cv2


chips = [] #chip array


boundariesColor = [
    ([83,200,205], [143,255,255]), #yellow bgr
    ([128,195,82], [198,255,152]), #light green
    ([52,76,134], [102,126,184]), #brown
    ([197,176,107], [255,236,167]), #lightblue
    ([141,125,23], [186,170,68])  #teal
]

color = ["yellow", "light green", "brown", "lightblue", "teal"]
colorCheck = []

file = open("text.txt", 'w')
#105 height of chip

# get the webcam as an object
#camera = cv2.VideoCapture(1)

# Capture frame-by-frame
#ret, frame = camera.read()

# Our operations on the frame come here

frame = cv2.imread("chipshack.jpg")
print(frame)
# Display the resulting frame
cv2.imshow('frame',frame)
#cv2.waitKey(0)

stackImage = frame[265:795, 135:1015] #cropping photo [vertical, horizontal]
cv2.imwrite("croppedPicture.jpg", stackImage)

#stackImage = cv2.imread("croppedPicture.jpg")

for x in range(1,6):
   chips.append(stackImage[((x-1)*105):x*105, 0:880])
   cv2.imwrite("chip%d.jpg" % x, chips[x-1])


for x in range(1,6):
    chips[x-1][0:100, 0:880]
    for (lower, upper) in boundariesColor:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype= "uint8")

        mask = cv2.inRange(chips[x-1], lower, upper)
        file.write(str(mask))
        colorCheck.append(cv2.countNonZero(mask))

        output = cv2.bitwise_and(chips[x-1], chips[x-1], mask=mask)

        cv2.imshow("images", np.hstack([chips[x-1],output]))
        cv2.waitKey(0)

    index = colorCheck.index(max(colorCheck))
    colorCheck = []
    print color[index]
    #print (color[index])
   # print("next chip")

print (colorCheck)
for x in range(1,6):
   chips.append(stackImage[((x-1)*12):11*x, 0:112])
   cv2.imwrite("chip%d.jpg" % x, chips[x-1])

# When everything done, release the capture
#camera.release()
#cv2.destroyAllWindows()

file.close()
