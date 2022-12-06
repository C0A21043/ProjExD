import tkinter as tk
#練習1
root=tk.Tk()
root.title("迷えるこうかとん")
image=tk.PhotoImage(file="fig/3.png")
canvas=tk.Canvas(width=1500,height=900,bg="black")
cx,cy=300,400
canvas.create_image(cx,cy,image=image)
canvas.pack()
root.mainloop()