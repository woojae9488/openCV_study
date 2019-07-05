import numpy as np
import cv2


def bitOperation(hpos, vpos):
    img1 = cv2.imread('images/model.png')
    img2 = cv2.imread('images/logo.png')

    # 로고를 사진 왼쪽 윗부분에 두기 위한 영역 지정
    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    # 로고를 위한 마스크와 역마스크 생성
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # ROI에서 로고에 해당하는 부분만 검정색으로 생성
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # 로고에서 로고 부분만 추출
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # 로고 배경을 cv2.add로 투명으로 만들고 ROI에 로고 넣기
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


bitOperation(10, 10)
