
import cv2

def picFun():

    img = cv2.imread("lena.jpg", flags= 1)
    #img ar upor line use kora
    img = cv2.line(img, (350, 0), (350, 500), (255, 222, 0), 5)

    #img ar upor arrow use kora
    img = cv2.arrowedLine(img, (0, 0), (300, 300), (0, 0, 255), 3)

    img = cv2.circle(img, (300, 300), 100, (0, 255, 0), -1)

    img = cv2.putText(img, "Selim", (200, 500), cv2.FONT_HERSHEY_COMPLEX_SMALL, 4, (0, 255, 255), 2, cv2.LINE_4)

    cv2.imshow("Lena Picture", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

picFun()