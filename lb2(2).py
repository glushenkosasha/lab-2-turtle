import turtle
import time
import math


class Digit:
    def __init__(self, digit, size=20):
        self.digit = digit
        self.size = size
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.penup()
        self.digit_map = {
            0: ((0, 1), (1, 0), (1, 2), (2, 1), (0, 0), (0, 2)),
            1: ((1, 2), (1, 0)),
        }

    def draw(self, x, y):
        self.pen.goto(x, y)
        for dot in self.digit_map[self.digit]:
            self.pen.goto(x + dot[0] * self.size, y + dot[1] * self.size)
            self.pen.dot(self.size // 2)


class ClockFace:
    def __init__(self):
        self.digits = []

    def add_digit(self, digit):
        self.digits.append(digit)

    def draw(self):
        for digit in self.digits:
            digit.draw(0, 0)


class Hand:
    def __init__(self, length, width=3):
        self.length = length
        self.width = width
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.pendown()
        self.pen.setheading(90)

    def draw(self, angle):
        self.pen.setheading(angle)
        self.pen.pensize(self.width)
        self.pen.forward(self.length)
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.pendown()


class Clock:
    def __init__(self, size=200):
        self.size = size
        self.window = turtle.Screen()
        self.window.setup(width=600, height=600)
        self.window.title("Analog Clock")
        self.clock_face = ClockFace()
        self.hour_hand = Hand(size * 0.5)
        self.minute_hand = Hand(size * 0.8)
        self.second_hand = Hand(size * 0.9, width=1)
        self.clock_face.add_digit(Digit(1))
        self.clock_face.draw()

    def update(self):
        while True:
            current_time = time.localtime()
            hours = current_time.tm_hour % 12
            minutes = current_time.tm_min
            seconds = current_time.tm_sec

            hour_angle = (hours / 12) * 360 + (minutes / 60) * 30
            minute_angle = (minutes / 60) * 360
            second_angle = (seconds / 60) * 360

            self.hour_hand.draw(-hour_angle)
            self.minute_hand.draw(-minute_angle)
            self.second_hand.draw(-second_angle)

            time.sleep(1)
            self.window.update()


clock = Clock()
clock.update()
turtle.done()
