
import turtle
d={"shape":"square","angle":90,"size":100,"color":"red"}
for i in range(4):
    turtle.pencolor(d["color"])
    turtle.shape(d["shape"])
    turtle.forward(d["size"])
    turtle.right(d["angle"])