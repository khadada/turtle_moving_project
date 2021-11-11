from turtle import Turtle, Screen

yk = Turtle()


def forword_fun():
    yk.forward(10)


def backword_fun():
    yk.backward(10)


def turn_left():
    yk.left(10)


def turn_right():
    yk.right(10)


def clear_c():
    yk.penup()
    yk.clear()
    yk.home()
    yk.pendown()


screen = Screen()
screen.listen()
screen.onkey(fun=forword_fun, key="z")
screen.onkey(fun=backword_fun, key="s")
screen.onkey(fun=turn_left, key="q")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_c, key="c")

screen.exitonclick()
