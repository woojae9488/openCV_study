import cv2
import numpy as np


def writeVideo():
    try:
        print('카메라를 구동')
        cap = cv2.VideoCapture('videos/testvideo.mp4')
    except:
        print('카메라 구동 실패')
        return

    fps = 20.0
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    out = cv2.VideoWriter('mycam.avi', fcc, fps, (width, height))
    print('녹화를 시작')

    while True:
        ret, frame = cap.read()

        if not ret:
            print('비디오 읽기 오류')
            break
        frame = cv2.flip(frame, 0) # 상하 반전

        cv2.imshow('video', frame)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('녹화를 종료')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


writeVideo()
