from turtle import Turtle
# constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def create_segment() -> Turtle:
    segment = Turtle(shape='square')
    segment.color('white')
    segment.penup()
    return segment


class Snake:
    def __init__(self):
        self.segments = []
        for position in STARTING_POSITION:
            segment = create_segment()
            segment.goto(position)
            self.segments.append(segment)
        self.head = self.segments[0]

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment = create_segment()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)