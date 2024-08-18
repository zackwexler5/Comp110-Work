"""My turtle scene that I am creating is a starry night. It includes the ground, stars, the moon, and trees. I decided to create this scene becuase I like to look at the sky during the night, and I thought this would look really cool."""

__author__ = "730678249"

from turtle import Turtle, colormode, done
import random
tommy: Turtle = Turtle()
tommy.screen.bgcolor("black")
tommy.speed(0)  
colormode(255)
tommy.color(99, 204, 250)


def draw_stars(Turtle: Turtle, x: float, y: float, size: float) -> None:
    """It draws a star at a given (x, y) position."""
    Turtle.penup()
    Turtle.goto(x, y)
    Turtle.pendown()
    Turtle.color("yellow")
    sides = 5
    angle: int = 144
    side_length = size
    for i in range(sides):
        Turtle.forward(side_length)
        Turtle.right(angle)
    Turtle.penup()
    return None


def draw_moon(Turtle: Turtle, x: float, y: float, radius: float) -> None:
    """It draws the moon at a given (x, y) position."""
    Turtle.penup()
    Turtle.goto(x, y)
    Turtle.pendown()
    Turtle.color("white")
    Turtle.begin_fill()
    Turtle.circle(radius)
    Turtle.end_fill()
    Turtle.penup()
    Turtle.hideturtle()
    return None


def draw_trees(Turtle: Turtle, x: float, y: float, trunk_width: float) -> None:
    """It draws all of the trees that are displauyed at the bottom of the screen."""
    trunk_length = 20
    Turtle.setheading(0)
    Turtle.penup()
    Turtle.goto(x - trunk_width / 2, y)
    Turtle.pendown()
    Turtle.color("brown")
    Turtle.begin_fill()
    i = 0
    while i < 2:
        Turtle.forward(trunk_width)
        Turtle.left(90)
        Turtle.forward(trunk_length)
        Turtle.left(90)
        i += 1
    Turtle.end_fill()
    leaf_length = 40
    Turtle.penup()
    Turtle.goto(x - (leaf_length) / 2, y + trunk_length)
    Turtle.pendown()
    Turtle.color("green")
    Turtle.begin_fill()
    i = 0
    while i < 3:
        Turtle.forward(leaf_length)
        Turtle.left(120)
        i += 1
    Turtle.end_fill()
    Turtle.hideturtle()
    Turtle.penup()
    return None


def draw_ground(Turtle: Turtle, x: float, y: float) -> None:
    """Draws the ground at the given coordinates."""
    Turtle.penup()
    Turtle.goto(x, y)
    Turtle.pendown()
    Turtle.color("darkgreen")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.forward(850)
        Turtle.left(90)
        Turtle.forward(40)
        Turtle.left(90)
    Turtle.end_fill()
    Turtle.penup()
    return None


def main() -> None:
    """Contains all of the call statements for the functions."""
    draw_moon(tommy, 350, 300, 50)
    draw_ground(tommy, -430, -406)
    for _ in range(150):  
        x = random.randint(-400, 400)
        y = random.randint(-350, 400)
        size = random.randint(5, 20)
        draw_stars(tommy, x, y, size)
    for i in range(50):
        x = random.randint(-400, 400)
        y = random.randint(-365, -365)
        draw_trees(tommy, x, y, 5)


if __name__ == "__main__":
    main()       
done()