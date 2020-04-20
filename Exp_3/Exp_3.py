import random
import turtle
siriux = turtle.Turtle()
protocol = turtle.Screen()
protocol.bgcolor("black")
siriux.pencolor("Red")

for x in range(5):
    a = 0
    b = 0

    rand_1 = random.randrange(-300,300)
    rand_2 = random.randrange(-300,300)
    siriux.speed(10)
    siriux.penup()
    siriux.setpos((rand_1,rand_2))
    siriux.pendown()

    while True:
        siriux.forward(a)
        siriux.right(b)
        a +=2
        b +=1
        if b == 205:
            break

turtle.done()































































# siriux.color("Black","Red")

# siriux.forward(100)
# siriux.left(90)

# siriux.begin_fill()

# siriux.forward(100)
# siriux.right(90)
# siriux.forward(100)
# siriux.right(90)
# siriux.forward(100)
# siriux.right(90)
# siriux.forward(100)

# siriux.end_fill()

# siriux.penup()
# siriux.left(90)
# siriux.forward(100)
# siriux.pendown()
