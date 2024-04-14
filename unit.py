from turtle import Turtle

class Unit(Turtle):
    def __init__(self, pos, scrn):
        super().__init__()
        
        self.setpos(pos)
        self.shape('square')
        self.color('green')
        self.penup()
        self.pn = scrn.textinput("Name", "Player Name")
        
        self.hideturtle()
        self.goto(pos[0], pos[1] - 15)
        self.write(self.pn, align="center", font=("Arial", 10, "normal"))
        self.goto(pos[0], pos[1] + 15)
        self.showturtle()
        
    def go_up(self):
        new_y = self.ycor() + 22
        self.hideturtle()
        self.goto(self.xcor(), new_y - 25)
        self.clear()
        self.write(self.pn, align="center", font=("Arial", 10, "normal"))
        self.goto(self.xcor(), new_y)
        self.showturtle()
        print(self.pos())

    def go_left(self):
        new_x = self.xcor() - 22
        self.hideturtle()
        self.goto(new_x, self.ycor() - 25)
        self.clear()
        self.write(self.pn, align="center", font=("Arial", 10, "normal"))
        self.goto(new_x, self.ycor() + 25)
        self.showturtle()
        
    def go_right(self):
        new_x = self.xcor() + 22
        self.hideturtle()
        self.goto(new_x, self.ycor() - 25)
        self.clear()
        self.write(self.pn, align="center", font=("Arial", 10, "normal"))
        self.goto(new_x, self.ycor() + 25)
        self.showturtle()

    def go_down(self):
        new_y = self.ycor() - 22
        self.hideturtle()
        self.goto(self.xcor(), new_y - 25)
        self.clear()
        self.write(self.pn, align="center", font=("Arial", 10, "normal"))
        self.goto(self.xcor(), new_y)
        self.showturtle()
        