import numpy as np
import cv2


def erodeNdilation():
    img = cv2.imread('images/alphabet.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3, 3), np.uint8)

    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow('original', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def openNclose():
    img1 = cv2.imread('images/a.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/b.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def otherMorph():
    img1 = cv2.imread('images/alphabet.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/a.jpg', cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('images/b.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3, 3), np.uint8)

    grad = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img3, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow('grad', grad)
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def makeKernel():
    M1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    M2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    M3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    print(M1)
    print(M2)
    print(M3)


makeKernel()
