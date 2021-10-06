import tkinter
from tkinter import messagebox
import turtle



def gay():
    turtle.Screen()
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle.begin_fill()

    for i in range(len(colors)):
        turtle.begin_fill()
        for j in range(2):
            turtle.fillcolor(colors[i])
            turtle.forward(250)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.pendown()
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()


def bi():
    turtle.Screen()
    colors = ["#D00070", "#8C4799", "#0032A0"]
    turtle.begin_fill()

    turtle.begin_fill()
    for i in range(len(colors)):
        turtle.begin_fill()
        for j in range(2):
            turtle.fillcolor(colors[i])
            turtle.forward(150)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.pendown()
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()

def pan():
    colors = ["#FF218C", "#FFD800", "#21B1FF"]
    turtle.Screen()

    turtle.begin_fill()

    for i in range(len(colors)):
        turtle.begin_fill()
        for j in range(2):
            turtle.fillcolor(colors[i])
            turtle.forward(150)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.pendown()
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()



def ace():
    turtle.Screen()
    colors = ["#000000", "#A4A4A4", "#FFFFFF", "#810081"]

    turtle.begin_fill()

    for i in range(len(colors)):
        turtle.begin_fill()
        for j in range(2):
            turtle.fillcolor(colors[i])
            turtle.forward(200)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.pendown()
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()


def trans():
    turtle.Screen()
    colors = ["#55CDFC", "#F7A8B8", "#FFFFFF", "#F7A8B8", "#55CDFC"]
    turtle.begin_fill()

    for i in range(len(colors)):
        turtle.begin_fill()
        for j in range(2):
            turtle.fillcolor(colors[i])
            turtle.forward(200)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.pendown()


def nonbinary():
    turtle.Screen()
    colors = ["#FFF430", "#FFFFFF", "#9C59D1", "#000000"]
    turtle.begin_fill()

    for i in range(len(colors)):
        turtle.begin_fill()
        for j in range(2):
            turtle.fillcolor(colors[i])
            turtle.forward(150)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.pendown()

def aro():
    colors = ["#3AA63F", "#A8D47A", "#FFFFFF", "#AAAAAA", "#000000"]
    turtle.begin_fill()

    turtle.begin_fill()

    for i in range(len(colors)):
        turtle.begin_fill()
        for j in range(2):
            turtle.fillcolor(colors[i])
            turtle.forward(200)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.pendown()
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()




class GUI:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()

        self.identitet1 = tkinter.Label(self.hovedvindu, text="Sexual Attraction:")
        self.identitet1.grid(column=0, row=1)

        self.var = tkinter.IntVar()

        self.gay = tkinter.Radiobutton(self.hovedvindu, text="homosexual", variable=self.var, value=1)
        self.gay.grid(column=1, row=1, columnspan=2)

        self.bi = tkinter.Radiobutton(self.hovedvindu, text="bisexual", variable=self.var, value=2)
        self.bi.grid(column=1, row=2, columnspan=2)

        self.pan = tkinter.Radiobutton(self.hovedvindu, text="pansexual", variable=self.var, value=3)
        self.pan.grid(column=1, row=3, columnspan=2)

        self.ace = tkinter.Radiobutton(self.hovedvindu, text="asexual", variable=self.var, value=4)
        self.ace.grid(column=1, row=4, columnspan=2)

        self.straight = tkinter.Radiobutton(self.hovedvindu, text="heterosexual", variable=self.var, value=5)
        self.straight.grid(column=1, row=5, columnspan=2)

        self.identitet2 = tkinter.Label(self.hovedvindu, text="Romantic attraction Attraction:")
        self.identitet2.grid(column=0,row=6)

        self.var2 = tkinter.IntVar()

        self.gay = tkinter.Radiobutton(self.hovedvindu, text="homoromantic", variable=self.var2, value=1)
        self.gay.grid(column=1, row=7, columnspan=2)

        self.bi = tkinter.Radiobutton(self.hovedvindu, text="biromantic", variable=self.var2, value=2)
        self.bi.grid(column=1, row=8, columnspan=2)

        self.pan = tkinter.Radiobutton(self.hovedvindu, text="panromantic", variable=self.var2, value=3)
        self.pan.grid(column=1, row=9, columnspan=2)

        self.ace = tkinter.Radiobutton(self.hovedvindu, text="aromantic", variable=self.var2, value=4)
        self.ace.grid(column=1, row=10, columnspan=2)

        self.straight = tkinter.Radiobutton(self.hovedvindu, text="heteroromantic", variable=self.var2, value=5)
        self.straight.grid(column=1, row=11, columnspan=2)

        self.identitet3 = tkinter.Label(self.hovedvindu, text="Gender identity:")
        self.identitet3.grid(column=0,row=12)

        self.var3 = tkinter.IntVar()

        self.trans = tkinter.Radiobutton(self.hovedvindu, text="trans", variable=self.var3, value=1)
        self.trans.grid(column=1, row=13, columnspan=2)

        self.enby = tkinter.Radiobutton(self.hovedvindu, text="non-binary", variable=self.var3, value=2)
        self.enby.grid(column=1, row=14, columnspan=2)

        self.cis = tkinter.Radiobutton(self.hovedvindu, text="cis", variable=self.var3, value=3)
        self.cis.grid(column=1, row=15, columnspan=2)

        self.slette_knapp = tkinter.Button(self.hovedvindu, text="Remove choices", command=self.slette_metode)
        self.slette_knapp.grid(column=1, row=16)

        self.flag_button = tkinter.Button(self.hovedvindu, text="Generate flag", command=self.generate_flag)
        self.flag_button.grid(column=0, row=16)

        tkinter.mainloop()

    def slette_metode(self):
        self.var.set(False)
        self.var2.set(False)
        self.var3.set(False)

    def generate_flag(self):
        identitet1 = self.var.get()
        identitet2 = self.var2.get()
        identitet3 = self.var3.get()

        turtle.hideturtle()
        
        if identitet1 == 0 or identitet2 == 0 or identitet3 == 0:
            messagebox.showerror("Mistake", "You need to select a radiobutton for all of the three identities!")
        else:
            if identitet1 == 1:
                turtle.penup()
                turtle.left(180)
                turtle.forward(250)
                turtle.right(90)
                turtle.forward(250)
                turtle.right(90)
                turtle.pendown()
                gay()

            elif identitet1 == 2:
                turtle.penup()
                turtle.left(180)
                turtle.forward(250)
                turtle.right(90)
                turtle.forward(250)
                turtle.right(90)
                turtle.pendown()
                bi()

            elif identitet1 == 3:
                turtle.penup()
                turtle.left(180)
                turtle.forward(250)
                turtle.right(90)
                turtle.forward(250)
                turtle.right(90)
                turtle.pendown()
                pan()

            elif identitet1 == 4:
                turtle.penup()
                turtle.left(180)
                turtle.forward(250)
                turtle.right(90)
                turtle.forward(250)
                turtle.right(90)
                turtle.pendown()
                ace()
            else:
                pass

            if identitet2 == identitet1:
                pass
            elif identitet2 == 1:
                gay()
            elif identitet2 == 2:
                bi()
            elif identitet2 == 3:
                pan()
            elif identitet2 == 4:
                aro()
            else:
                pass

            if identitet3 == 1:
                trans()
            elif identitet3 == 2:
                nonbinary()
            else:
                pass

            if identitet1 == 5 and identitet3 == 3 and identitet2 == 5:
                messagebox.showinfo("cishet", "I'm so sorry that you're cisgender and straight. Hopefully you get better soon :)")

            self.hovedvindu.destroy()


if __name__ == "__main__":
    gui = GUI()



