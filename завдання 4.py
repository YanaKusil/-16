from tkinter import *

root = Tk()
canvas = Canvas(root, width=700, height=500)
canvas.pack()

# Небо
canvas.create_rectangle(0, 0, 700, 300, fill="skyblue")

# Сонце
canvas.create_oval(550, 50, 620, 120, fill="yellow", outline="orange")

# Трава (береги)
canvas.create_rectangle(0, 300, 700, 400, fill="lightgreen")

# Річка
canvas.create_rectangle(0, 350, 700, 500, fill="deepskyblue")

# Дерево (просте)
canvas.create_rectangle(100, 250, 115, 320, fill="sienna")  # Стовбур
canvas.create_oval(80, 200, 135, 270, fill="forestgreen")   # Крона

# Хатинка
canvas.create_rectangle(400, 280, 470, 350, fill="burlywood")      # Стіни
canvas.create_polygon(400, 280, 435, 240, 470, 280, fill="brown")  # Дах
canvas.create_rectangle(420, 310, 440, 340, fill="white")          # Вікно
canvas.create_rectangle(450, 320, 465, 350, fill="sienna")         # Двері

root.mainloop()