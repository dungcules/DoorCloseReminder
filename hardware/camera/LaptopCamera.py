import cv2

from CameraInterface import CamInterface

class LaptopCam(CamInterface):
    def __init__(self):
        self.camera = None
        print("Init camera...")
        
    def connectTo(self):
        print("Start init camera...")
        self.camera = cv2.VideoCapture(0)
        
        if not self.camera.isOpened():
            print("Cannot open camera!")
            return
        
    def show_camera(self):
        print("Start camera...")
        while True:
            # Capture frame-by-frame
            ret, frame = self.camera.read()

            # If frame is read correctly, ret is True
            if not ret:
                print("Can't receive frame")
                break

            # Display the frame in a window
            cv2.imshow('Camera Stream', frame)

            # Press 'q' to exit the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def terminate(self):
        print("Terminating laptop camera...")
        self.camera.release()
        cv2.destroyAllWindows()
    