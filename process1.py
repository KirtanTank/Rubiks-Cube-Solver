from ColorDetection import detect as dt
from CubeMap import cube_map as cm
import cv2


color_dict = {}
# color_list = ["red", "orange", "yellow", "blue", "white", "green"]

for i in range(6):
    y = dt()
    center = y[4]
    # print(center)
    color_dict[center] = y

cv2.destroyAllWindows()

# print(color_dict)
cm(color_dict)
