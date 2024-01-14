
from turtle import Turtle, Screen
# "r" to reset!


tod = Turtle()
screen = Screen()


# TODO 1: W to go Forwards
def move_forwards():
    tod.forward(20)


# TODO 2: S to go Backwards
def move_backwards():
    tod.backward(20)

# TODO 3: A to go Counter-Clockwise
def rotate_counter_clockwise():
    tod.left(8)


# TODO 3: A to go Counter-Clockwise
def rotate_clockwise():
    tod.right(8)


# TODO 5: C to Clear the drawing, and go back to the Center of the screen
def shake_etch_a_sketch():
    tod.clear()
    tod.penup()
    tod.home()
    tod.pendown()
    #could also use tod.reset() for all of these, but currently it's safer, longer term to preserve variable data.



screen.listen()  #it must listen first before triggering functions with key-typing
#to trigger the function in the moment a key is pressed, remove the additional ()  !!
screen.onkey(fun=move_forwards, key="Up")
screen.onkey(fun=move_backwards, key="Down")
screen.onkey(fun=rotate_counter_clockwise, key="Left")
screen.onkey(fun=rotate_clockwise, key="Right")
screen.onkey(fun=shake_etch_a_sketch, key="r")


screen.exitonclick()


# from turtle import Turtle, Screen
#
#
# tod = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     tod.forward(10)
#
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forward)  #function, which makes it move forward :D
# screen.exitonclick()