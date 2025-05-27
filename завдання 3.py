import tkinter as tk

root = tk.Tk ()
canvas = tk.Canvas (root, width=600, height=600, bg="white")
canvas.pack()

#Прямо задаємо три точки (х1, у1, х2, у2, х3, у3, x4, y4)
canvas.create_polygon( 200, 200,300, 200,350, 300,250, 300,fill="pink", outline="red")
canvas.create_oval(100, 100, 200, 200, fill='skyblue', outline='black')
root.mainloop()