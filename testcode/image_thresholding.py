import numpy as np
import cv2
import matplotlib.pyplot as plt


def globalThresholding():
    img = cv2.imread('images/model.png', cv2.IMREAD_GRAYSCALE)

    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('original', img)
    cv2.imshow('BINARY', thr1)
    cv2.imshow('BINARY_INV', thr2)
    cv2.imshow('TRUNC', thr3)
    cv2.imshow('TOZERO', thr4)
    cv2.imshow('TOZERO_INV', thr5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def adaptivethresholding():
    img = cv2.imread('images/model.png', cv2.IMREAD_GRAYSCALE)

    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    thr2 = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    thr3 = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    titles = [
        'original', 'Global Thresholding(v=127)', 'Adaptive MEAN', 'Adaptive GAUSSIAN']
    images = [img, thr1, thr2, thr3]

    for i in range(4):
        cv2.imshow(titles[i], images[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def thresholding():
    img = cv2.imread('images/model.png', cv2.IMREAD_GRAYSCALE)

    # 전역 thresholding 적용
    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Otsu 바이너리제이션
    ret, thr2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # 가우시안 블러 적용 후 Otsu 바이너리제이션
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, thr3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    titles = ['original noisy', 'Histogram', 'G-Thresholding',
              'original noisy', 'Histogram', 'Otsu Thresholding',
              'Gaussian-filtered', 'Histogram', 'Otsu Thresholding']

    images = [img, 0, thr1, img, 0, thr2, blur, 0, thr3]

    for i in range(3):
        plt.subplot(5, 4, i*3+1)
        plt.imshow(images[i*3], 'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

        plt.subplot(5, 4, i*3+2), plt.hist(images[i*3].ravel(), 256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])

        plt.subplot(5, 4, i*3+3), plt.imshow(images[i*3+2], 'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

    plt.show()


thresholding()
