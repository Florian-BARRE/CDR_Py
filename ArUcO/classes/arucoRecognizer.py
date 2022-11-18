import cv2
import numpy as np


class FrameDetection:
    def __init__(self, ids: list[int], corners: list[np.array]):
        self.ids = ids
        self.corners = corners


class ArucoRecognizer:

    def __init__(self, dict_type: str):
        self._aruco_dict = cv2.aruco.Dictionary_get(getattr(cv2.aruco, dict_type))
        self._aruco_params = cv2.aruco.DetectorParameters_create()

    def detect(self, frame: np.ndarray, **extra_params) -> FrameDetection:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_founded = cv2.aruco.detectMarkers(gray, self._aruco_dict, parameters=self._aruco_params, **extra_params)
        return FrameDetection(aruco_founded[1], aruco_founded[0])


def draw_markers(frame: np.ndarray, detectobj: FrameDetection) -> np.ndarray:
    if detectobj.ids:
        frame = cv2.aruco.drawDetectedMarkers(frame, detectobj.corners, detectobj.ids)
    return frame


"""

webcam = Camera()
arucoParams = cv2.aruco.DetectorParameters_create()
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)


while True:
    frame = webcam.Read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, arucoDict, parameters=arucoParams)
    cv2.aruco.drawDetectedMarkers(frame, corners)

    #found = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
    #corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict, parameters=parameters, cameraMatrix=matrix_coefficients, distCoeff=distortion_coefficients)

    print(f"Corners: {corners}")
    print(f"Ids: {ids}")
    print(f"rejected_img_points: {rejected_img_points}")
    print()

    frame_markers = cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    if corners:
        radius = 5
        thickness = 2

        cv2.circle(
            frame_markers,
            (int(corners[0][0][0][0]), int(corners[0][0][0][1])),
            radius,
            (255, 0, 0),
            thickness
        )
        cv2.circle(
            frame_markers,
            (int(corners[0][0][1][0]), int(corners[0][0][1][1])),
            radius,
            (0, 255, 0),
            thickness
        )
        cv2.circle(
            frame_markers,
            (int(corners[0][0][2][0]), int(corners[0][0][2][1])),
            radius,
            (0, 0, 255),
            thickness
        )

    webcam.Update_Monitor(frame_markers)

"""
