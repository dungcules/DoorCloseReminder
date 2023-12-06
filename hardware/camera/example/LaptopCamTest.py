import sys
sys.path.append('../')

from LaptopCamera import LaptopCam

#if __name__ == "__main__":
lap_cam = LaptopCam()
lap_cam.connectTo()
lap_cam.show_camera()
lap_cam.terminate()
