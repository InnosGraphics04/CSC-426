import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get().replace("^", "**")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("CSC426 Calculator")
root.geometry("350x450")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('%',4,1), ('^',4,2), ('+',4,3)
]

for (text,row,col) in buttons:
    tk.Button(
        root,
        text=text,
        width=8,
        height=3,
        command=lambda t=text: click(t)
    ).grid(row=row,column=col)

tk.Button(root,text='C',width=16,height=3,bg='orange',
          command=clear).grid(row=5,column=0,columnspan=2)

tk.Button(root,text='=',width=16,height=3,bg='lightgreen',
          command=calculate).grid(row=5,column=2,columnspan=2)

root.mainloop()