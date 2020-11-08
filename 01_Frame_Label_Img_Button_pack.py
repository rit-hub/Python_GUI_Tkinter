from tkinter import *
root = Tk()
root.title("First Project")

root.geometry("1200x980")
frame=Frame(root,bg="#E8F6F3",borderwidth="16",)
l1=Label(frame,text="Darknight",bg="#E8F6F3", font ="monospace 19 bold",padx=5,pady=10,fg="purple")

l1.pack()

frame.pack(fill=X)
frame2=Frame(root,bg="#E8F6F3",borderwidth="12", )

b1=Button(frame2, fg="black", text="install",font="20")
b1.pack()

frame2.pack(side=LEFT,anchor="ne",fill=Y)


frame3=Frame(root,bg="#E8F6F3", borderwidth="15")
frame3.pack(side= RIGHT)
photo=PhotoImage(file="includes/p1.png")
p1=Label(frame3,image=photo)
p1.pack(side=LEFT)
root.mainloop()