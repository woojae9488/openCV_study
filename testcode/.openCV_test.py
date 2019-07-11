from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

# 명령행 인자 구성 및 파서 생성
ap = argparse.ArgumentParser()
ap.add_argument('-v', '--video', type=str, help='path to input video file')
ap.add_argument('-t', '--tracker', type=str, default='kcf',
                help='OpenCV object tracker type')
args = vars(ap.parse_args())

# OpenCV 버전을 얻어낸다.
(major, minor) = cv2.__version__.split('.')[:2]

# OpenCV 버전 3.2이하이면 우리는 트래킹을 위해 특별한 개체를 사용해야 한다.
if int(major) == 3 and int(minor) < 3:
    tracker = cv2.Tracker_create(args['tracker'].upper())
# OpenCV 버전 3.3이상이면 우리는 적절한 트래킹 생성자를 호출한다.
else:
    # 트래킹 구현을 위한 여러 트래킹 사전을 만든다.(enum같은 것)
    OPENCV_OBJECT_TRACKERS = {
        'csrt': cv2.TrackerCSRT_create,
        'kcf': cv2.TrackerKCF_create,
        'boosting': cv2.TrackerBoosting_create,
        'mil': cv2.TrackerMIL,
        'tld': cv2.TrackerTLD_create,
        'medianflow': cv2.TrackerMedianFlow_create,
        'mosse': cv2.TrackerMOSSE_create
    }

    # 명령행 인자로 넘겨준 트래킹 네임을 가지고 적절한 트래커를 생성한다.
    tracker = OPENCV_OBJECT_TRACKERS[args['tracker']]()

# 우리가 추적할 객체의 경계 박스를 초기화한다.
initBB = None

# 비디오 경로가 지정되어 있지 않으면 기본 웹캠으로 동영상을 바꾼다.
if not args.get('video', False):
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(1.0)
# 비디오 경로가 지정되어 있으면 그걸 사용한다.
else:
    vs = cv2.VideoCapture(args['video'])

# 우리가 추정할 fps를 초기화한다.
fps = None

# 동영상 스트림의 프레임 반복 시작
while True:
    # 현재 프레임의 작업들을 시작한다.
    frame = vs.read()
    frame = frame[1] if args.get('video', False) else frame

    # 동영상 스트림이 모두 끝났는지 확인한다.
    if frame is None:
        break

    # 프레임 크기를 재조정하고 프레임 비율을 맞춘다.
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]

    # 우리가 현재 추적을 하고 있는지 확인한다.
    if initBB is not None:
        # 객체의 새로운 경계 박스를 지정한다.
        (success, box) = tracker.update(frame)

        # 트래킹이 성공적으로 되었는지 확인한다.
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # fps 값을 갱신시킨다.
        fps.update()
        fps.stop()

        # 우리가 프레임 화면상에 출력시킬 정보를 초기화한다.
        info = [
            ('Tracker', args['tracker']),
            ('Success', 'yes' if success else 'No'),
            ('FPS', '{:.2f}'.format(fps.fps())),
        ]

        # 출력시킬 정보들을 출력시킨다.
        for (i, (k, v)) in enumerate(info):
            text = '{}: {}'.format(k, v)
            cv2.putText(frame, text, (10, H-((i*20)+20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255, 2))

    # 출력 프레임을 보여준다.
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF

    # s키가 눌러지면 추적할 경계 박스를 선택할 수 있다.
    if key == ord('s'):
        # 우리가 추적하길 원하는 객체를 선택하고 엔터나 스페이스바를 누르면 ROI가 선택된다.
        initBB = cv2.selectROI(
            'Frame', frame, fromCenter=False, showCrosshair=True)
        # 주어진 경계 박스를 사용해 OpenCV 객체 추적을 시작한다.
        # fps 처리량 추정기도 시작한다.
        tracker.init(frame, initBB)
        fps = FPS().start()

    # q키가 눌러지면 반복문을 벗어난다.
    elif key == ord('q'):
        break

# 웹 캠을 사용했었다면 포인터를 해제시킨다.
if not args.get('video', False):
    vs.stop()
# 아니면 파일 포인터를 해제시킨다.
else:
    vs.release()

# 모든 윈도우 창을 닫고 끝낸다.
cv2.destroyAllWindows()
