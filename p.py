# Import Required Library
from tkinter import *
import tkinter.messagebox as tmsg
import random


def gui():
    print("* * * * * * * * * * * * * * welcome to the game * * * * * * * * * * * * * * * * * *")
    print("! ! ! plese see   the gui window to play the game! ! ! ")
gui()


 
# Create Object
root = Tk()
 
# Set geometry [we can also give root.minisize(300,400) root.maxisize(200,300)]

root.geometry("600x700")
root.wm_iconbitmap("a.ico")
root.configure(background="grey")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")

# Set title
root.title("Rock Paper Scissor Game")




# Computer Value
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}
 
# Reset The Game 
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    
    l1.config(text="Player              ",fg="green")
    l3.config(text="Computer",fg="red")
    l4.config(text="please select the button",fg="blue")
    
    

 
 
# Disable the Button
 
 
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    
x=Label(root,text="welcome to the game",font="bold 20 bold",fg="green",width=30,bg="black")
x.place(x=500,y=10)
  


## this is to creat dropdown menus
def myfunc():
    
    a=tmsg.showinfo("other games","please buy our games on play store and app store " )
    print(a)
def msg():
    a = tmsg.showinfo("help"," we help you please send your problem to this email address:21bt04062@gsfcuniversity.ac.in")
    print(a)
def msg0():
    
    a = tmsg.askquestion("review","was you enjoy my gui game?")
    print(a)
    
def save():
    a= tmsg.askquestion("save","do you want to save")
    print(a)
    button_disable()

a = Menu(root)
a.add_command(label="other game", command=myfunc)
a.add_command(label="help", command=msg)
a.add_command(label="exit", command=quit)
a.add_command(label="save game", command=save)
a.add_command(label="review", command=msg0)

root.config(menu=a)
    

# If player selected rock
def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "You Win"
    else:
        match_result = "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=c_v)
    
    button_disable()
    
    
# If player selected paper
 
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "You  Win"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=c_v)
    
    button_disable()
 
# If player selected scissor

def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result ="You Win"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=c_v)
    button_disable()
ispaper
 
# Add Labels, Frames and Button
Label(root,
      text="Rock Paper Scissor",
      font="bold 20 bold",
      fg="blue").pack(pady=60)
 
frame = Frame(root,borderwidth=10,relief=SOLID,)
frame.pack(side=TOP,
           pady=20,
           padx=10,)
 
l1 = Label(frame,
           text="Player              ",
           font="bold 20 bold",
           fg="green",
           pady=10 ,
           padx=10,
           bg="black")
 
l2 = Label(frame,
           text="VS             ",
           font="bold 20 bold",
           padx=30,
           pady=10,
           bg="black",fg="blue")
 
l3 = Label(frame, text="Computer",fg="red", font="bold 20 bold",padx=10,pady=10,bg="black")


 
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()


l4 = Label(root,
           text="PLEASE SELECT THE BUTTON",font="bold 50 bold",bg="white",width=35,
           fg="blue",borderwidth=10,relief="solid",padx=10)
l4.pack(pady=20)

     
b1 = Button(root, text="Rock",
            font='arial 20 bold', width=5,
            command=isrock,padx=40,fg='white',bg='orange',borderwidth=5,relief=SUNKEN,)

b2 = Button(root, text="Paper ",
            font='arial 35 bold', width=7,
            command=ispaper,padx=40,fg='orange',bg='white',borderwidth=5,relief=SUNKEN,)
 
b3 = Button(root, text="Scissor",
            font='arial 35 bold', width=5,
            command=isscissor,padx=40, fg='white',bg='light green',borderwidth=5,relief=SUNKEN)
def Exit():
    print("you exited game successfully the game")
    print("* * *thanks for playing the game * * *")
    root.destroy()
Button(root, font = 'arial 25 bold', text = 'EXIT'  ,padx =5,bg ='seashell4',fg='red' ,command = Exit).place(x=520,y=700,width=500,height=70)
b1.place(x=350,y=400,width=300,height=100)
b2.place(x=635,y=500,width=300,height=100)
b3.place(x=910,y=400,width=300,height=100)


Button(root, text="Reset Game", font='bold 25', fg="red",bg="black", command=reset_game).place( x=520,y=600,width=500, height=100)

root.mainloop()
#
#important nots :
# in pack()  we can use anchor = nw   [hear nw is north west] 
#grid layout contain rows we can deefine grid layout i.e:b1.gried(row=1,col=1)but hear we can't becaus we allready usepack 
# grid layoutis just like pack,place
 #4 types of variables 1.boolian,2.string,3.int,4.double

#a=stringvar()
#Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)



#a = 800
#b = 400
#root.geometry(f"{a}x{b}")
# c=Canvas(root,width=a,height=b)
#c.pack()
#the lines goes from the point x1,y1 to x2,y2
#c.create_line(0,0,400,10) 

# Execute Tkinter
##multiple menus
""" b = Menu(root)
c = Menu(b)
c.add_command(label="new game", command = myfunc)
c.add_command(label="exit", command = myfunc)
c.add_command(label="load game", command = myfunc)
c.add_command(label="other games", command = myfunc)
c.add_command(label="review", command = myfunc)
root.config(menu=c)

c.add_cascade(label="file",menu=c) """