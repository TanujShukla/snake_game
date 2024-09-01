from turtle import Turtle,Screen
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:

    def __init__(self):
        self.sagments = []
        self.create_snake()
        self.head=self.sagments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_sagmnet(position)

    def reset(self):
        for seg in self.sagments:
            seg.goto(1000,1000)
        self.sagments.clear()
        self.create_snake()
        self.head = self.sagments[0]


    def add_sagmnet(self,position):
        new_sagment = Turtle()
        new_sagment.shape("square")
        new_sagment.color("white")
        new_sagment.penup()
        new_sagment.goto(position)
        self.sagments.append(new_sagment)

    def move(self):
        for seg_num in range(len(self.sagments) - 1, 0, -1):
            new_x = self.sagments[seg_num - 1].xcor()
            new_y = self.sagments[seg_num - 1].ycor()
            self.sagments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)




    def extend(self):
        self.add_sagmnet(self.sagments[-1].position())


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)





