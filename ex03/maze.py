import tkinter as tk

def key_down(event):
    global key
    key=event.keysym
    

if __name__ == "__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")
    image=tk.PhotoImage(file="fig/3.png")
    canvas=tk.Canvas(width=1500,height=900,bg="black")
    cx,cy=300,400
    canvas.create_image(cx,cy,image=image)
    canvas.pack()
    key=""
    root.bind("<KeyPress>",key_down)
    root.mainloop()