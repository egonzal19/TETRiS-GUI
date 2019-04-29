import tkinter

####Definitions for the Buttons####
def client_quit():
    exit()

#####Buttons#####
root = tkinter.Tk()

HEIGHT = 700
WIDTH= 800

Canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
Canvas.pack()

Frame= tkinter.Frame(root, bg='black')
Frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

Label= tkinter.Label(Frame,text="TETRiS",fg="salmon",bg='#add8e6',font=("Arial Bold", 80))
Label.place(relx=.1,rely=.1,relheight=.3,relwidth=.8)

Button = tkinter.Button(Frame, text="Start")
Button.place(relx=0.2,rely=0.5,relheight=.2,relwidth=.6)

quitButton = tkinter.Button(Frame, text = "Quit", command = client_quit)
quitButton.place(relx=0.2,rely=0.8, relheight=.15, relwidth=.6)


root.mainloop()
