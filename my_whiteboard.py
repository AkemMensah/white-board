import tkinter as tk
from tkinter.colorchooser import askcolor

# Defining the func that tracts the initial point
def draw_now(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x,event.y

# defining func to keep tract of pointer positions
def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = current_x, current_y

# Func that prompt drawing to stop
def stop_drawing(event):
    global is_drawing
    is_drawing = False

# func that allows pen color change
def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color

# func to determine line width
def change_line_width(value):
    global line_width
    line_width = int(value)

# Defining the app features
root = tk.Tk()
root.title("Easy Whiteboard")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

is_drawing = False
drawing_color = "blue"
line_width = 2

root.geometry("600x500")

# frame to hold the buttons or controls in the same line.
controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")

# two buttons for control for color and clearing
color_button = tk.Button(controls_frame, text="Change Color", command=change_pen_color)
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all"))

color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)

# slider for the line width function
line_width_label = tk.Label(controls_frame, text="Line Width:")
line_width_label.pack(side="left", padx=5, pady=5)

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))
line_width_slider.set(line_width)
line_width_slider.pack(side="left", padx=5, pady=5)

# Text widget for notes
text_widget_label = tk.Label(controls_frame, text="Notes:")
text_widget_label.pack(side="top", padx=5, pady=5)
text_widget = tk.Text(controls_frame, height=6, width=120)
text_widget.pack(side="left", padx=5, pady=5)

# connect features with the GUI.
# link the functions with the buttons and controls created
canvas.bind("<Button-1>", draw_now)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()
