from turtle import Screen, write, clear, Turtle
from unit import Unit
from variables import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Battler')
screen.listen()
# screen.tracer(0)

#draw lines
drawer = Turtle()
drawer.color("white")
drawer.penup()
# drawer.hideturtle()
drawer.goto(-400, 285)
drawer.speed(15)

drawer.color('green')
for i in range(0, 35):
    
    drawer.write(f"{i}", align="center", font=("Arial", 8, "normal"))
    drawer.forward(22)
drawer.right(90)

drawer.color('blue')

for i in range(1, 28):
    
    drawer.write(f"{i}", align="center", font=("Arial", 8, "normal"))
    drawer.forward(22)
    
drawer.right(90)
drawer.pencolor("#766306")

for i in range(27):
    drawer.pendown()
    drawer.forward(800)
    drawer.right(180)
    drawer.penup()
    presx = drawer.xcor()
    presy = drawer.ycor()

    drawer.goto(presx, presy + 22)
    
drawer.setheading(270)

for i in range(36):
    drawer.pendown()
    drawer.forward(800)
    presx = drawer.xcor()
    presy = drawer.ycor()
    drawer.penup()
    drawer.goto(presx + 22, presy)
    drawer.left(180)
    
drawer.hideturtle()
screen._turtles.pop()

units = []

  
def get_mouseclick(x, y):
    # print(x, y)
    unit = Unit((x, y), screen)
    screen.listen()
    screen.update()
    units.append(unit)
    print(screen._turtles)
    

def detect_click(x, y):
    # print(x, y)
    for i in range(len(units)):
        # print(units[i].pos())
        unit_x = int(units[i].xcor())
        unit_y = int(units[i].ycor())
        if x in range(unit_x - 20, unit_x + 20) and y in range(unit_y - 20, unit_y + 20):
            print(f"This is the position of the unit: {units[i].pos()}")
            active_unit = units[i]
            screen.onkey(active_unit.go_up, 'w')
            screen.onkey(active_unit.go_down, 's')
            screen.onkey(active_unit.go_left, 'a')
            screen.onkey(active_unit.go_right, 'd')
            
def measure(coords, unit):
    print('ckic')
    distance = unit.distance(coords)
    print(distance)

def aggressor_on_click(x, y):
    for i in range(len(units)):
        # print(units[i].pos())
        unit_x = int(units[i].xcor())
        unit_y = int(units[i].ycor())
        if x in range(unit_x - 20, unit_x + 20) and y in range(unit_y - 20, unit_y + 20):
            aggressor = units[i]
        print(aggressor)

def switch_to_targetting():
    screen.onscreenclick(lambda x, y: aggressor_on_click(x, y), btn=1)

screen.onscreenclick(get_mouseclick, btn=3)
screen.onscreenclick(detect_click)

screen.onkeypress(switch_to_targetting,'f')

screen.mainloop()
