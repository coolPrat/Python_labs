__author__ = 'pratik'

"""
CSCI-603: Intro Lecture (week 1)
Author: Pratik kulkarni (psk7534@g.rit.edu)

This program draws the String 'I am pratik'.
It reuses letter I and A.

"""

import turtle
import math


def init():
    """
    Initialize for drawing. take the turtle to (-350,0)
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: None
    """
    turtle.penup()
    turtle.setpos(-350,0)
    turtle.left(90)


def space():
    """
    Adds a space of 25 pixels. This acts as a logical separator between two words.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (25,0), heading (north), up
    :return: None
    """
    turtle.up()
    turtle.setposition(turtle.xcor()+25, 0)


def draw_letter_p():
    """
    Draw the letter P
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(70)


def draw_letter_r():
    """
    Draw the letter R
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(math.sqrt(5000))
    turtle.penup()
    turtle.left(45)
    turtle.forward(20)
    turtle.left(90)


def draw_letter_a():
    """
    Draw the letter A
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.back(50)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)


def draw_latter_t():
    """
    Draw the letter T
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.back(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)


def draw_latter_i():
    """
    Draw the letter I
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    turtle.setposition(turtle.xcor()+50, 100)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.back(50)
    turtle.penup()
    turtle.back(20)
    turtle.right(90)


def draw_latter_k():
    """
    Draw the letter K
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    turtle.pendown()
    turtle.forward(100)
    turtle.penup()
    turtle.setposition(turtle.xcor()+50, 100)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(math.sqrt(5000))
    turtle.left(90)
    turtle.forward(math.sqrt(5000))
    turtle.penup()
    turtle.left(45)
    turtle.forward(20)
    turtle.left(90)


def draw_letter_m():
    """
    Draw the letter M
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)
    turtle.back(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)


def main():
    """
    Draws 'I am pratik'
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (20,0), heading (north), up
    :return: None
    """
    init()
    draw_latter_i()
    space()
    draw_letter_a()
    draw_letter_m()
    space()
    draw_letter_p()
    draw_letter_r()
    draw_letter_a()
    draw_latter_t()
    draw_latter_i()
    draw_latter_k()
    turtle.hideturtle()


if __name__ == '__main__':
    main()
    input("Press Enter to close")
