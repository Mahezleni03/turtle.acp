import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle : Square")

my_pen = turtle.Turtle()

for i in range(4):
    my_pen.forward(100)
    my_pen.right(90)