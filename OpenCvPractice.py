
import cv2
import numpy as np

def picture_abiBaki_hai():

    img = cv2.imread("lena.jpg", flags= -1)
    print(img)
    print(np.shape(img))
    print(np.max(img))
    print(np.min(img))

    cv2.imshow("lena picture", img)
    key = cv2.waitKey() & 0xFF
    if key == 27:
        print("The window is shutdown")
        cv2.destroyAllWindows()
    elif key == ord("s"):

        cv2.imwrite("lena_copy2.png", img)
        #cv2.waitKey(0)
        cv2.destroyAllWindows()

def videoCap():

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        #gry = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("amar Video", frame)

        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    #picture_abiBaki_hai()
    videoCap()

if __name__ == "__main__":
    main()