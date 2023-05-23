from tkinter import *
from tkinter import font


# import ColorDetection as dt


def cube_map(req_dict=None):
    window = Tk()
    if req_dict is None:
        req_dict = {'R': ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                    'Y': ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                    'O': ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                    'W': ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                    'B': ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                    'G': ['-', '-', '-', '-', '-', '-', '-', '-', '-']}
    window.title("Cube Map")
    window.geometry("850x680+50+50")
    print(req_dict)

    pos_list = [[4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6], [6, 4], [6, 5], [6, 6],  # Front
                [4, 7], [4, 8], [4, 9], [5, 7], [5, 8], [5, 9], [6, 7], [6, 8], [6, 9],  # Right
                [4, 10], [4, 11], [4, 12], [5, 10], [5, 11], [5, 12], [6, 10], [6, 11], [6, 12],  # Back
                [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 2], [6, 3],  # Left
                [1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6],  # Up
                [7, 4], [7, 5], [7, 6], [8, 4], [8, 5], [8, 6], [9, 4], [9, 5], [9, 6],  # Bottom
                ]

    # Create a dictionary to map colors to letters
    color_map = {'R': 'red', 'G': 'green', 'O': 'orange', 'B': 'blue', 'Y': 'yellow', 'W': 'white'}

    k = 0
    for i, face in enumerate(('R', 'Y', 'O', 'W', 'B', 'G')):
        for j in range(9):
            # Get the color for the current cell
            color = color_map.get(req_dict[face][j], 'pink')

            # Create a canvas for the current cell and set its background color
            if j == 4:
                canvas = Canvas(window, bg=color, height="50", width="50", highlightbackground="black",
                                highlightthickness=5)
            else:
                canvas = Canvas(window, bg=color, height="50", width="50")

            # # Calculate the row and column for the current cell
            # row = j // 3 + i // 3 * 3
            # col = j % 3 + i % 3 * 3  # Reverse the order of the columns

            # Add the canvas to the grid
            canvas.grid(row=pos_list[k][0], column=pos_list[k][1])
            k += 1

            # Add a label to the center of the canvas for certain cells
            if j == 4:
                if face == 'R':
                    canvas.create_text(28, 28, text="F", fill="black", font='Helvetica 20 bold')
                elif face == 'Y':
                    canvas.create_text(28, 28, text="R", fill="black", font='Helvetica 20 bold')
                elif face == 'O':
                    canvas.create_text(28, 28, text="B", fill="black", font='Helvetica 20 bold')
                elif face == 'W':
                    canvas.create_text(28, 28, text="L", fill="black", font='Helvetica 20 bold')
                elif face == 'B':
                    canvas.create_text(28, 28, text="U", fill="black", font='Helvetica 20 bold')
                elif face == 'G':
                    canvas.create_text(28, 28, text="D", fill="black", font='Helvetica 20 bold')

    myFont = font.Font(size=15)
    button = Button(window, text='OK', bg='#0052cc', fg='#ffffff', command=window.destroy)
    button['font'] = myFont
    button.grid(row=15, column=15)

    window.mainloop()
