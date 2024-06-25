import random as r
import turtle as t

num_of_steps = 0
try:
    num_of_steps = int(t.textinput("Make Your Bet", "Who will win the race"))
except :
    num_of_steps = 0

# num_of_steps =  int(input("Enter the number of steps of Turtle : "))
class Motion:
    def __init__(self, turtle):
        self.t = turtle

    def left(self):
        self.t.left(90)
        self.t.fd(20)

    def right(self):
        self.t.right(90)
        self.t.fd(20)

    def forward(self):
        self.t.fd(20)

    def backward(self):
        self.t.fd(-20)

    def random_color(self):
        self.r = r.randint(0, 255)
        self.g = r.randint(0, 255)
        self.b = r.randint(0, 255)
        return tuple((self.r, self.g, self.b))


timmy = t.Turtle()
screen = t.Screen()
timmy.shape("circle")
screen.bgcolor("skyblue")
timmy.color("yellow")
timmy.shapesize(0.5)
timmy.pensize(8)
timmy.speed(10)
motion = Motion(timmy)
t.colormode(255)
lst = [motion.forward, motion.backward, motion.left, motion.right]
for i in range(num_of_steps):
    fun = r.choice(lst)
    # timmy.color(r.choice(color))
    timmy.color(motion.random_color())
    fun()

screen.exitonclick()
