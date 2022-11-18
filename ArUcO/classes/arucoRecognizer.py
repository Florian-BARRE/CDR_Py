import cv2
import numpy as np


class FrameDetection:
    def __init__(self, ids: list[int], corners: list[np.array]):
        self.ids = ids
        self.corners = corners
        self.len = 0 if ids is None else len(ids)


class ArucoRecognizer:

    def __init__(self, dict_type: str):
        self._aruco_dict = cv2.aruco.Dictionary_get(getattr(cv2.aruco, dict_type))
        self._aruco_params = cv2.aruco.DetectorParameters_create()

    def detect(self, frame: np.ndarray, **extra_params) -> FrameDetection:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_founded = cv2.aruco.detectMarkers(gray, self._aruco_dict, parameters=self._aruco_params, **extra_params)
        return FrameDetection(aruco_founded[1], aruco_founded[0])


def draw_markers(frame: np.ndarray, detectobj: FrameDetection) -> np.ndarray:
    if detectobj.len:
        frame = cv2.aruco.drawDetectedMarkers(frame, detectobj.corners, detectobj.ids)
    return frame
