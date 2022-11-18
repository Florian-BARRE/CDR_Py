from classes.camera import Camera
from classes.arucoRecognizer import ArucoRecognizer, draw_markers

webcam = Camera()
aruco_ia = ArucoRecognizer("DICT_4X4_100")

while True:
    frame = webcam.Read()
    founds = aruco_ia.detect(frame)
    marked_frame = draw_markers(frame, founds)

    webcam.Update_Monitor(marked_frame)
