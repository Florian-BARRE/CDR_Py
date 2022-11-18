from classes.camera import Camera
from classes.arucoRecognizer import ArucoRecognizer, draw_markers, draw_corners, draw_barycenter

webcam = Camera()
aruco_ia = ArucoRecognizer("DICT_4X4_100")

while True:
    frame = webcam.Read()
    founds = aruco_ia.detect(frame)
    marked_frame = draw_markers(frame, founds)
    draw_corners(frame, founds)
    draw_barycenter(frame, founds)

    webcam.Update_Monitor(marked_frame)



"""
radius = 5
thickness = 2

cv2.circle(
    frame_markers,
    (int(corners[0][0][0][0]), int(corners[0][0][0][1])),
    radius,
    (255, 0, 0),
    thickness
)
"""