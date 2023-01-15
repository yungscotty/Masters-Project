import cv2 as cv
import numpy as np

def main():
    windowName = "Line Detection"
    cv.namedWindow(windowName)
    cap = cv.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    img_counter = 0

    while ret:
        ret, frame = cap.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (27,27), 0)
        #blur = cv.medianBlur(gray, 27)
        edges = cv.Canny(blur, 50, 250, apertureSize=5, L2gradient=True)
        
        lines = cv.HoughLinesP(edges, 1, np.pi/180, 80, maxLineGap=12, minLineLength=100)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv.line(frame, (x1,y1), (x2, y2), (0,0,255), 2)


        cv.imshow(windowName, frame)

        k = cv.waitKey(1)
        if k%256 == 27:     # exit on ESC
            break
        elif k%256 == 32:   # screenshot on space
            img_name = "opencv_screenshot_{}.png".format(img_counter)
            cv.imwrite(img_name, frame)
            print("{} saved!".format(img_name))
            img_counter += 1

    cv.destroyAllWindows()
 
    cap.release()

if __name__ == '__main__':
    main()