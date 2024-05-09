import tkinter
from tkinter import *

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print(screen_height, screen_width)
window.geometry(f"{screen_width - 10}x{screen_height - 90}+0+0")
window.resizable(False, False)  # Make window non-resizable

# Create the frame with desired background color
parent_frame = Frame(window, bg='#000000',height=screen_height,width=screen_width)

main_frame = Frame(parent_frame, bg="#11DFBD", height=400, width=300)
window.grid_columnconfigure(0, minsize=200, pad=30)
# Place the frame within the window (using pack() in this example)
parent_frame.grid(row=1,column=1)
main_frame.grid(row=2, column=2)
window.mainloop()

