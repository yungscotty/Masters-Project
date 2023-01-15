import cv2 as cv
import numpy as np

img = cv.imread('Photos/Doorway2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(gray, 9)
edges = cv.Canny(blur, 50, 200)

lineCounter = 0
doorCounter = 0

# Hough line transform method:
lines = cv.HoughLinesP(edges, 1, np.pi/180, 40, maxLineGap=5, minLineLength=15)

for line in lines:
    x1, y1, x2, y2 = line[0]
    p1, p2 = (x1,y1), (x2,y2)

    # find line length
    length = np.linalg.norm(tuple(map(lambda i, j: i - j, p1, p2)))

 # if line is longer than 100pix
    if 100<length<130:
        doorFrameX = x1,x2
        doorFrameY = y1,y2


        cv.line(img, p1, p2, (255,255,0), 2) # make it blue

 # if line is shorter than 100pix
    else:
        cv.line(img, p1, p2, (0,255,0), 2) # make it green

    # draw circles on endpoints of lines
    cv.circle(img, p1, 2, (0,0,255), cv.FILLED)
    cv.circle(img, p2, 2, (0,0,255), cv.FILLED)

    lineCounter += 1


## Noisy image
image = cv.imread('Photos/Doorway2.jpg')
# Add Gaussian noise
noise = np.random.randn(*image.shape) * 60
n_img = image + noise

# Clip the pixel values to the range [0, 255]
n_img = np.clip(n_img, 0, 255)

# Convert the pixel values to integers
n_img = np.uint8(n_img)

gray_n = cv.cvtColor(n_img, cv.COLOR_BGR2GRAY)
blur_n = cv.medianBlur(gray_n, 9)
edges_n = cv.Canny(blur_n, 50, 200)

n_lineCounter = 0
n_doorCounter = 0

# Hough line transform method:
n_lines = cv.HoughLinesP(edges_n, 1, np.pi/180, 40, maxLineGap=5, minLineLength=15)

for line in n_lines:
    x1, y1, x2, y2 = line[0]
    p1, p2 = (x1,y1), (x2,y2)

    # find line length
    length = np.linalg.norm(tuple(map(lambda i, j: i - j, p1, p2)))

 # if line is longer than 100pix
    if 100<length<130:
        doorFrameX = x1,x2
        doorFrameY = y1,y2


        cv.line(n_img, p1, p2, (0,255,0), 2) # make it blue, no - green!

 # if line is shorter than 100pix
    else:
        cv.line(n_img, p1, p2, (0,255,0), 2) # make it green

    # draw circles on endpoints of lines
    cv.circle(n_img, p1, 2, (0,0,255), cv.FILLED)
    cv.circle(n_img, p2, 2, (0,0,255), cv.FILLED)

    n_lineCounter += 1


# uk standard interior door dimsensions: 1981mm x 762mm which is basically a 2.6:1 height to width ratio

# identify door in image
# search for groups of lines of same length which are parallel to each other, then filter by the door width (using ratio)
# to find which side the top is, whichever side has a line (since ground is rarely detected)





cv.imshow('Image', img)
cv.imshow("Noisy Image", n_img)
# cv.imshow('Edges', edges)
print('Detected', lineCounter, 'lines in image!')
print('Detected', n_lineCounter, 'lines in noisy image!')
# print('Detected', doorCounter, 'doors in image!')
cv.waitKey(0)
cv.destroyAllWindows()


cv.imwrite('C:/Users/scott/Pictures/Saved Pictures/linedoor60.png', n_img)
print('image was successfully saved')