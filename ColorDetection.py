import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


def detect():
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = frame.shape

        cx1 = int(width / 1.12)
        cy1 = int(height / 1.5)

        cx2 = int(width / 1.29)
        cy2 = int(height / 1.5)

        cx3 = int(width / 1.5)
        cy3 = int(height / 1.5)

        cx4 = int(width / 1.12)
        cy4 = int(height / 1.28)

        cx5 = int(width / 1.29)
        cy5 = int(height / 1.28)

        cx6 = int(width / 1.5)
        cy6 = int(height / 1.28)

        cx7 = int(width / 1.12)
        cy7 = int(height / 1.1)

        cx8 = int(width / 1.29)
        cy8 = int(height / 1.1)

        cx9 = int(width / 1.5)
        cy9 = int(height / 1.1)

        # Pick Pixel Value
        pixel_center1 = rgb_frame[cy1, cx1]
        pixel_center2 = rgb_frame[cy2, cx2]
        pixel_center3 = rgb_frame[cy3, cx3]
        pixel_center4 = rgb_frame[cy4, cx4]
        pixel_center5 = rgb_frame[cy5, cx5]
        pixel_center6 = rgb_frame[cy6, cx6]
        pixel_center7 = rgb_frame[cy7, cx7]
        pixel_center8 = rgb_frame[cy8, cx8]
        pixel_center9 = rgb_frame[cy9, cx9]

        rgb_value1 = pixel_center1
        rgb_value2 = pixel_center2
        rgb_value3 = pixel_center3
        rgb_value4 = pixel_center4
        rgb_value5 = pixel_center5
        rgb_value6 = pixel_center6
        rgb_value7 = pixel_center7
        rgb_value8 = pixel_center8
        rgb_value9 = pixel_center9

        color1 = ""
        color2 = ""
        color3 = ""
        color4 = ""
        color5 = ""
        color6 = ""
        color7 = ""
        color8 = ""
        color9 = ""

        color_list = [color1, color2, color3, color4, color5, color6, color7, color8, color9]

        # POINT 1
        if (rgb_value1[0] > rgb_value1[1]) and (rgb_value1[0] > rgb_value1[2]) and (rgb_value1[1] < 100) and (
                rgb_value1[2] < 100):
            color1 = "R"
            color_list[0] = color1
        elif (rgb_value1[0] >= 220) and (rgb_value1[1] >= 220) and (rgb_value1[2] < 180):
            color1 = "Y"
            color_list[0] = color1
        elif (rgb_value1[0] > rgb_value1[1]) and (rgb_value1[1] > rgb_value1[2]):
            color1 = "O"
            color_list[0] = color1
        elif (rgb_value1[0] >= 200) and (rgb_value1[1] >= 200) and (rgb_value1[2] >= 200):
            color1 = "W"
            color_list[0] = color1
        elif (rgb_value1[1] > rgb_value1[0]) and (rgb_value1[1] > rgb_value1[2]):
            color1 = "G"
            color_list[0] = color1
        elif (rgb_value1[2] > rgb_value1[0]) and (rgb_value1[2] > rgb_value1[1]):
            color1 = "B"
            color_list[0] = color1
        else:
            color1 = "Y"
            color_list[0] = color1

        # POINT 2
        if (rgb_value2[0] > rgb_value2[1]) and (rgb_value2[0] > rgb_value2[2]) and (rgb_value2[1] < 120) and (
                rgb_value2[2] < 120):
            color2 = "R"
            color_list[1] = color2
        elif (rgb_value2[0] >= 220) and (rgb_value2[1] >= 220) and (rgb_value2[2] < 180):
            color2 = "Y"
            color_list[1] = color2
        elif (rgb_value2[0] > rgb_value2[1]) and (rgb_value2[1] > rgb_value2[2]):
            color2 = "O"
            color_list[1] = color2
        elif (rgb_value2[0] >= 200) and (rgb_value2[1] >= 200) and (rgb_value2[2] >= 200):
            color2 = "W"
            color_list[1] = color2
        elif (rgb_value2[1] > rgb_value2[0]) and (rgb_value2[1] > rgb_value2[2]):
            color2 = "G"
            color_list[1] = color2
        elif (rgb_value2[2] > rgb_value2[0]) and (rgb_value2[2] > rgb_value2[1]):
            color2 = "B"
            color_list[1] = color2
        else:
            color2 = "Y"
            color_list[1] = color2

        # POINT 3
        if (rgb_value3[0] > rgb_value3[1]) and (rgb_value3[0] > rgb_value3[2]) and (rgb_value3[1] < 120) and (
                rgb_value3[2] < 120):
            color3 = "R"
            color_list[2] = color3
        elif (rgb_value3[0] >= 220) and (rgb_value3[1] >= 220) and (rgb_value3[2] < 180):
            color3 = "Y"
            color_list[2] = color3
        elif (rgb_value3[0] > rgb_value3[1]) and (rgb_value3[1] > rgb_value3[2]):
            color3 = "O"
            color_list[2] = color3
        elif (rgb_value3[0] >= 200) and (rgb_value3[1] >= 200) and (rgb_value3[2] >= 200):
            color3 = "W"
            color_list[2] = color3
        elif (rgb_value3[1] > rgb_value3[0]) and (rgb_value3[1] > rgb_value3[2]):
            color3 = "G"
            color_list[2] = color3
        elif (rgb_value3[2] > rgb_value3[0]) and (rgb_value3[2] > rgb_value3[1]):
            color3 = "B"
            color_list[2] = color3
        else:
            color3 = "Y"
            color_list[2] = color3

        # POINT 4
        if (rgb_value4[0] > rgb_value4[1]) and (rgb_value4[0] > rgb_value4[2]) and (rgb_value4[1] < 120) and (
                rgb_value4[2] < 120):
            color4 = "R"
            color_list[3] = color4
        elif (rgb_value4[0] >= 220) and (rgb_value4[1] >= 220) and (rgb_value4[2] < 180):
            color4 = "Y"
            color_list[3] = color4
        elif (rgb_value4[0] > rgb_value4[1]) and (rgb_value4[1] > rgb_value4[2]):
            color4 = "O"
            color_list[3] = color4
        elif (rgb_value4[0] >= 200) and (rgb_value4[1] >= 200) and (rgb_value4[2] >= 200):
            color4 = "W"
            color_list[3] = color4
        elif (rgb_value4[1] > rgb_value4[0]) and (rgb_value4[1] > rgb_value4[2]):
            color4 = "G"
            color_list[3] = color4
        elif (rgb_value4[2] > rgb_value4[0]) and (rgb_value4[2] > rgb_value4[1]):
            color4 = "B"
            color_list[3] = color4
        else:
            color4 = "-"
            color_list[3] = color4

        # POINT 5
        if (rgb_value5[0] > rgb_value5[1]) and (rgb_value5[0] > rgb_value5[2]) and (rgb_value5[1] < 120) and (
                rgb_value5[2] < 120):
            color5 = "R"
            color_list[4] = color5
        elif (rgb_value5[0] >= 220) and (rgb_value5[1] >= 220) and (rgb_value5[2] < 180):
            color5 = "Y"
            color_list[4] = color5
        elif (rgb_value5[0] > rgb_value5[1]) and (rgb_value5[1] > rgb_value5[2]):
            color5 = "O"
            color_list[4] = color5
        elif (rgb_value5[0] >= 200) and (rgb_value5[1] >= 200) and (rgb_value5[2] >= 200):
            color5 = "W"
            color_list[4] = color5
        elif (rgb_value5[1] > rgb_value5[0]) and (rgb_value5[1] > rgb_value5[2]):
            color5 = "G"
            color_list[4] = color5
        elif (rgb_value5[2] > rgb_value5[0]) and (rgb_value5[2] > rgb_value5[1]):
            color5 = "B"
            color_list[4] = color5
        else:
            color5 = "-"
            color_list[4] = color5

        # POINT 6
        if (rgb_value6[0] > rgb_value6[1]) and (rgb_value6[0] > rgb_value6[2]) and (rgb_value6[1] < 120) and (
                rgb_value6[2] < 120):
            color6 = "R"
            color_list[5] = color6
        elif (rgb_value6[0] >= 220) and (rgb_value6[1] >= 220) and (rgb_value6[2] < 180):
            color6 = "Y"
            color_list[5] = color6
        elif (rgb_value6[0] > rgb_value6[1]) and (rgb_value6[1] > rgb_value6[2]):
            color6 = "O"
            color_list[5] = color6
        elif (rgb_value6[0] >= 200) and (rgb_value6[1] >= 200) and (rgb_value6[2] >= 200):
            color6 = "W"
            color_list[5] = color6
        elif (rgb_value6[1] > rgb_value6[0]) and (rgb_value6[1] > rgb_value6[2]):
            color6 = "G"
            color_list[5] = color6
        elif (rgb_value6[2] > rgb_value6[0]) and (rgb_value6[2] > rgb_value6[1]):
            color6 = "B"
            color_list[5] = color6
        else:
            color6 = "-"
            color_list[5] = color6

        # POINT 7
        if (rgb_value7[0] > rgb_value7[1]) and (rgb_value7[0] > rgb_value7[2]) and (rgb_value7[1] < 120) and (
                rgb_value7[2] < 120):
            color7 = "R"
            color_list[6] = color7
        elif (rgb_value7[0] >= 220) and (rgb_value7[1] >= 220) and (rgb_value7[2] < 180):
            color7 = "Y"
            color_list[6] = color7
        elif (rgb_value7[0] > rgb_value7[1]) and (rgb_value7[1] > rgb_value7[2]):
            color7 = "O"
            color_list[6] = color7
        elif (rgb_value7[0] >= 200) and (rgb_value7[1] >= 200) and (rgb_value7[2] >= 200):
            color7 = "W"
            color_list[6] = color7
        elif (rgb_value7[1] > rgb_value7[0]) and (rgb_value7[1] > rgb_value7[2]):
            color7 = "G"
            color_list[6] = color7
        elif (rgb_value7[2] > rgb_value7[0]) and (rgb_value7[2] > rgb_value7[1]):
            color7 = "B"
            color_list[6] = color7
        else:
            color7 = "-"
            color_list[6] = color7

        # POINT 8
        if (rgb_value8[0] > rgb_value8[1]) and (rgb_value8[0] > rgb_value8[2]) and (rgb_value8[1] < 120) and (
                rgb_value8[2] < 120):
            color8 = "R"
            color_list[7] = color8
        elif (rgb_value8[0] >= 220) and (rgb_value8[1] >= 220) and (rgb_value8[2] < 180):
            color8 = "Y"
            color_list[7] = color8
        elif (rgb_value8[0] > rgb_value8[1]) and (rgb_value8[1] > rgb_value8[2]):
            color8 = "O"
            color_list[7] = color8
        elif (rgb_value8[0] >= 200) and (rgb_value8[1] >= 200) and (rgb_value8[2] >= 200):
            color8 = "W"
            color_list[7] = color8
        elif (rgb_value8[1] > rgb_value8[0]) and (rgb_value8[1] > rgb_value8[2]):
            color8 = "G"
            color_list[7] = color8
        elif (rgb_value8[2] > rgb_value8[0]) and (rgb_value8[2] > rgb_value8[1]):
            color8 = "B"
            color_list[7] = color8
        else:
            color8 = "-"
            color_list[7] = color8

        # POINT 9
        if (rgb_value9[0] > rgb_value9[1]) and (rgb_value9[0] > rgb_value9[2]) and (rgb_value9[1] < 120) and (
                rgb_value9[2] < 120):
            color9 = "R"
            color_list[8] = color9
        elif (rgb_value9[0] >= 220) and (rgb_value9[1] >= 220) and (rgb_value9[2] < 180):
            color9 = "Y"
            color_list[8] = color9
        elif (rgb_value9[0] > rgb_value9[1]) and (rgb_value9[1] > rgb_value9[2]):
            color9 = "O"
            color_list[8] = color9
        elif (rgb_value9[0] >= 200) and (rgb_value9[1] >= 200) and (rgb_value9[2] >= 200):
            color9 = "W"
            color_list[8] = color9
        elif (rgb_value9[1] > rgb_value9[0]) and (rgb_value9[1] > rgb_value9[2]):
            color9 = "G"
            color_list[8] = color9
        elif (rgb_value9[2] > rgb_value9[0]) and (rgb_value9[2] > rgb_value9[1]):
            color9 = "B"
            color_list[8] = color9
        else:
            color9 = "-"
            color_list[8] = color9

        b1, g1, r1 = (int(pixel_center1[0]), int(pixel_center1[1]), int(pixel_center1[2]))
        b2, g2, r2 = int(pixel_center2[0]), int(pixel_center2[1]), int(pixel_center2[2])
        b3, g3, r3 = int(pixel_center3[0]), int(pixel_center3[1]), int(pixel_center3[2])
        b4, g4, r4 = int(pixel_center4[0]), int(pixel_center4[1]), int(pixel_center4[2])
        b5, g5, r5 = int(pixel_center5[0]), int(pixel_center5[1]), int(pixel_center5[2])
        b6, g6, r6 = int(pixel_center6[0]), int(pixel_center6[1]), int(pixel_center6[2])
        b7, g7, r7 = int(pixel_center7[0]), int(pixel_center7[1]), int(pixel_center7[2])
        b8, g8, r8 = int(pixel_center8[0]), int(pixel_center8[1]), int(pixel_center8[2])
        b9, g9, r9 = int(pixel_center9[0]), int(pixel_center9[1]), int(pixel_center9[2])

        color_dict = {
            'red': ['left', color1, color2, color3, color4, color5, color6, color7, color8, color9],
            'blue': ['front', color1, color2, color3, color4, color5, color6, color7, color8, color9],
            'orange': ['right', color1, color2, color3, color4, color5, color6, color7, color8, color9],
            'green': ['back', color1, color2, color3, color4, color5, color6, color7, color8, color9],
            'white': ['up', color1, color2, color3, color4, color5, color6, color7, color8, color9],
            'yellow': ['down', color1, color2, color3, color4, color5, color6, color7, color8, color9],
        }

        # print(pixel_center1, color1, "|", pixel_center2, color2, "|", pixel_center3, color3, "|",
        #       pixel_center4, color4, "|", pixel_center5, color5, "|", pixel_center6, color6, "|",
        #       pixel_center7, color7, "|", pixel_center8, color8, "|", pixel_center9, color9)

        cv2.putText(frame, color1, (cx1, cy1), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx1, cy1), 13, (b1, g1, r1), 4)

        cv2.putText(frame, color2, (cx2, cy2), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx2, cy2), 13, (b2, g2, r2), 4)

        cv2.putText(frame, color3, (cx3, cy3), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx3, cy3), 13, (b3, g3, r3), 4)

        cv2.putText(frame, color4, (cx4, cy4), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx4, cy4), 13, (b4, g4, r4), 4)

        cv2.putText(frame, color5, (cx5, cy5), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx5, cy5), 13, (b5, g5, r5), 4)

        cv2.putText(frame, color6, (cx6, cy6), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx6, cy6), 13, (b6, g6, r6), 4)

        cv2.putText(frame, color7, (cx7, cy7), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx7, cy7), 13, (b7, g7, r7), 4)

        cv2.putText(frame, color8, (cx8, cy8), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx8, cy8), 13, (b8, g8, r8), 4)

        cv2.putText(frame, color9, (cx9, cy9), 0, 1, (0, 0, 0), 2)
        cv2.circle(frame, (cx9, cy9), 13, (b9, g9, r9), 4)

        cv2.putText(frame, "Red: Front", (10, 30), 0, 1, (0, 1, 0), 1)
        cv2.putText(frame, "Yellow: Right", (10, 60), 0, 1, (0, 1, 0), 1)
        cv2.putText(frame, "Orange: Back", (10, 90), 0, 1, (0, 1, 0), 1)
        cv2.putText(frame, "White: Left", (300, 30), 0, 1, (0, 1, 0), 1)
        cv2.putText(frame, "Blue: Up", (300, 60), 0, 1, (0, 1, 0), 1)
        cv2.putText(frame, "Green: Down", (300, 90), 0, 1, (0, 1, 0), 1)

        cv2.imshow("Frame", frame)
        # cv2.imshow('mask', res)
        key = cv2.waitKey(1)
        if key == 27:
            break

        elif key == 32:
            print(color_list)
            return color_list

    cap.release()
    cv2.destroyAllWindows()
