import numpy as np
import cv2


def addImage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    add_img1 = img1+img2
    add_img2 = cv2.add(img1, img2)

    cv2.imshow('img1+img2', add_img1)
    cv2.imshow('add(img1, img2)', add_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def onMouse(x):
    pass


def imgBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('MIXING', 'ImgPane', 0, 100, onMouse)
    mix = cv2.getTrackbarPos('MIXING', 'ImgPane')

    while True:
        img = cv2.addWeighted(img1, float(100-mix)/100,
                              img2, float(mix)/100, 0)
        cv2.imshow('ImgPane', img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mix = cv2.getTrackbarPos('MIXING', 'ImgPane')
    cv2.destroyAllWindows()


addImage('images/model.png', 'images/model2.png')
imgBlending('images/model.png', 'images/model2.png')
