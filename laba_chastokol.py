import tkinter as tk
import tkinter.ttk as ttk
import json

window = tk.Tk()

label = tk.Label(
    text='початковий текст:',
    foreground='black',
    background='white'
)
label.pack()

entry = tk.Entry(fg='black', bg='white', width=25)
entry.pack()

label1 = tk.Label(
    text='ключ:',
    foreground='black',
    background='white'
)
label1.pack()

entry1 = tk.Entry(fg='black', bg='white', width=5)
entry1.pack()
def chastokol():
    part1=[]
    part2=[]
    entr1=entry1.get()
    entr1i=int(entr1)
    print(isinstance(entr1, str))

    entr=entry.get()
    entrl=list(entr)
    print(isinstance(entr, str))
    print(entr)
    i = 0
    resultat=""
    key=0 + entr1i
    lenword=len(entr)
    print (lenword)
    a=0
    key1=key
    for a in range(key):
        if a > 0:
              a=a+1
        if entr1i > 0:
            while i < len(entr):
                key = i + 1
                if key % entr1i == 0:
                    if(entrl[i] !=0):
                            part1.append(entrl[i])
                    entrl[i] = 0
                i += 1
            entr1i -= 1
    print(part1)
    label2 = tk.Label(
    text={resultat},
    foreground='black',
    background='white'
    )
    label2.pack()


button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="yellow",
    fg="black",
    command=chastokol
)
button.pack()

window.mainloop()
#він мав працювати але я навіть не розумію чому він не хоче( ну принаймі менюшка нормальна )