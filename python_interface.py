from tkinter import *
def event():
	
	# from intro import warning
	root = Tk(className="My first window")
	root.config(bg="black", width=1200, height=500)
	root.resizable(0, 0)
	
	frame = Frame(root)
	frame.place(x=390, y=0)
	frame.config(bg="#ddd", width=500, height=500)

	label = Label(frame)
	label.place(x=0, y=50)
	label.config(text="BANKING ACCOUNT", fg="#ddd", bg="#222", width=50, height=2, font="Verdana", bd=0, justify="center")

	label2 = Label(frame)
	label2.place(x=0, y=150)
	label2.config(text="Email", fg="#222", bg="#d1d1d1", width=50, height=2, font="Verdana", bd=0, justify="center")

	textEmail = Entry(frame)
	textEmail.place(x=120, y=200, width=300, height=35)
	textEmail.config(font="Verdana", fg="#222")
 

	textPassword = Entry(frame)
	textPassword.place(x=120, y=240, width=300, height=35)
	textPassword.config(font="Verdana", fg="#222", show=".", justify="center")

	buttonStart = Button(frame)
	buttonStart.place(x=180, y=300)
	buttonStart.config(width=20, height=2, bg="blue", fg="white", text="Start session")

	buttonRegister = Button(frame)
	buttonRegister.place(x=316, y=470)
	buttonRegister.config(width=20, height=1, bg="red", fg="white", text="Register")
	root.mainloop()




#calling to function event
event()
