import turtle
turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(width=500, height=500)
polygon=turtle.Turtle()
num_sides=6
length=70
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()