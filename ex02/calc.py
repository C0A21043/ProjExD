import tkinter as tk
#練習3
import tkinter.messagebox as tkm
root=tk.Tk()
#練習３
def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンがクリックされました")
    
    
    
#練習1
root.geometry("300x500")
#練習2
r,c=0,0
for num in range(9,-1,-1):
    button=tk.Button(root,text=f"{num}",width=4,height=2,font=("",30))
#練習3
    button.bind("<1>",button_click)    
    button.grid(row=r,column=c)
    c+=1
    if c%3==0:
        r+=1
        c=0
root.mainloop()
