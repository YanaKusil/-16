from tkinter import*
import winsound
from PIL import Image, ImageTk
def play():
    if var.get() == 0:
        winsound.PlaySound("5.wav", winsound.SND_FILENAME)
    elif var.get() == 1:
        winsound.PlaySound("6.wav", winsound.SND_FILENAME)
    elif var.get() == 2:
        winsound.PlaySound("7.wav", winsound.SND_FILENAME)
    elif var.get() == 3:
        winsound.PlaySound("8.wav", winsound.SND_FILENAME)
        
root=Tk()
root.minsize(width=300, height=600)
root.title("Словник")
root['bg']='white'
frame = LabelFrame(root, text="Виберіть слово", padx=5, bg="white",bd=3)
frame.pack()
var = IntVar()
var.set(0)
Radiobutton1 = Radiobutton(frame,bg="white",text="Цукерка на палочці",
    variable=var, value=0).pack(anchor="w")
Radiobutton2 = Radiobutton(frame,bg="white",text="Торт",
    variable=var, value=1).pack(anchor="w")
Radiobutton3 = Radiobutton(frame,bg="white",text="Млинці",
    variable=var, value=2).pack(anchor="w")
Radiobutton4 = Radiobutton(frame,bg="white",text="Печево",
    variable=var, value=3).pack(anchor="w")

button = Button(text="Відтворити",width=15, height=2,bg="yellow",command=play).pack()

canvas = Canvas(root,width=545,height=273,bg='white')
canvas.pack()
img = Image.open('sweets.png')
img = img.resize((550, 275))
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=NW)
canvas.image = img

root.mainloop()