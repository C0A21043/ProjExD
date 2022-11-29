import tkinter as tk
#練習3
import tkinter.messagebox as tkm
#練習３
def button_click(event):
    btn=event.widget
    txt=btn["text"]
#練習７
    if txt == "=":
        sushiki=entry.get()
        result=eval(sushiki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    elif txt =="c":
        entry.delete(0,tk.END)
    elif t
    else:
#練習６
        entry.insert(tk.END,txt)

        

    
    
    
#練習1
root=tk.Tk()
root.geometry("400x600")
#練習2
r,c=1,0
for num in range(9,-1,-1):
    button=tk.Button(root,text=f"{num}",width=4,height=2,font=("",30))
#練習3
    button.bind("<1>",button_click)    
    button.grid(row=r,column=c)
    c+=1
    if c%3==0:
        r+=1
        c=0
        
#練習４
entry=tk.Entry(justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)

#練習５
kigou=["+","=","-","x","÷","e","c",]
for kg in kigou:
    button=tk.Button(root,text=f"{kg}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c+=1
    if c%4==0:
        r+=1
        c=0
root.mainloop()
