import numpy as np
import cv2


def imgResize():
    img = cv2.imread('images/model.png')
    h, w = img.shape[:2]

    img2 = cv2.resize(img, None, fx=0.5, fy=1, interpolation=cv2.INTER_AREA)
    img3 = cv2.resize(img, None, fx=1, fy=0.5, interpolation=cv2.INTER_AREA)
    img4 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    cv2.imshow('original', img)
    cv2.imshow('fx=0.5', img2)
    cv2.imshow('fy=0.5', img3)
    cv2.imshow('fx=0.5, fy=0.5', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imgMove():
    img = cv2.imread('images/model.png')
    h, w = img.shape[:2]

    M = np.float32([[1, 0, 100], [0, 1, 50]])

    img2 = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('shift image', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imgRotation():
    img = cv2.imread('images/model.png')
    h, w = img.shape[:2]

    M1 = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)
    M2 = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)

    img2 = cv2.warpAffine(img, M1, (w, h))
    img3 = cv2.warpAffine(img, M2, (w, h))

    cv2.imshow('45-Rotated', img2)
    cv2.imshow('90-Rotated', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imgDistanceBy3P():
    img = cv2.imread('images/model.png')
    h, w = img.shape[:2]

    pts1 = np.float32([[50, 50], [200, 50], [20, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    img2 = cv2.warpAffine(img, M, (w, h))

    cv2.imshow('original', img)
    cv2.imshow('Affine-Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imgDistanceBy4P():
    img = cv2.imread('images/model.png')
    h, w = img.shape[:2]

    pts1 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    pts2 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    img2 = cv2.warpPerspective(img, M, (w, h))

    cv2.imshow('original', img)
    cv2.imshow('Perspective-Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


imgDistanceBy4P()
