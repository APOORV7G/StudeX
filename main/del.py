import tkinter as tk
def show_selected():
    selected = var.get()
    result_label.config(text=selected)
root = tk.Tk()
root.title("Radio Buttons Example")
var = tk.IntVar()
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
radio_button1.pack(anchor=tk.W)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
radio_button2.pack(anchor=tk.W)
radio_button3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3)
radio_button3.pack(anchor=tk.W)
check = tk.Checkbutton(root,text="Hi",command=show_selected)
check.pack()
result_label = tk.Label(root, text="")
result_label.pack(anchor=tk.W)
root.mainloop()