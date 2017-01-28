
"""
CSCI-603: Lab 2
Author-1: Pratik kulkarni (psk7534@g.rit.edu)

This program draws a forest and a house. Number of trees is taken as input from the use.
Type of the trees are selected at random while drawing them. User can specify if the house is present
initially. if it is present then the position is selected at random based on number of trees.
Initially it draws forest at night with trees, house nad moon.
After drawing forest at night it calculates the amount of timber available and uses it to make(draw)
bigger house during day time.
"""

import turtle
import random
import math

totalWood = 0
maxHeight = 0


def init():

    """
    Initialisation function which takes input from user
    and displays output.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (0,0), heading (east), right
    :return: None
    """

    global totalWood
    global maxHeight
    trees = int(input("How many trees in your forest?"))
    house = input("Is there a house in the forest (y/n)?")
    if(trees < 2 and house == "y"):
        print("we need atleast two trees for drawing house")
    else:
        turtle.penup()
        turtle.setposition(-330, -100)
        position_of_house = random.randint(1, trees - 1)
        counter = 0
        if house != "y":
            counter = counter + 1
        while counter <= trees :
            if counter == position_of_house and house == "y":
                y = drawHouse(100)
                totalWood = totalWood + y
                spaceBetween(counter, trees)
            else:
                type_of_tree = random.randint(1, 3)
                wood, height = drawTrees(type_of_tree)
                spaceBetween(counter, trees)
                totalWood = totalWood + wood
                if height > maxHeight:
                    maxHeight = height
            counter = counter + 1

        draw_star(maxHeight)
        turtle.hideturtle()
        input("Night is done, press enter for day")
        new_wall_size = calculate_wall_size(totalWood)
        print("We have " + str(totalWood) + " units of lumber for building.")
        print("We will build a house with walls " + str(new_wall_size) + " tall.")
        turtle.reset()
        turtle.penup()
        turtle.setposition(-250, -250)
        drawHouse(new_wall_size)
        draw_sun(3 * new_wall_size / 2)
        turtle.hideturtle()
        input("Day is done, house is built, press enter to quit")


def draw_star(ycor):

    """
    This is the function for drawing star which takes
    y coordinate as a input.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (ycor+40,0), heading (north), up
    :return: None
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(ycor+40)
    turtle.down()
    for x in range(0, 8):
        turtle.forward(30)
        turtle.back(30)
        turtle.left(45)
    turtle.up()



def drawHouse(wallSize):

    """
    This is the function for drawing house which takes
    wall size as a input.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (wallSize,0), heading (north), up
    :return: total wood required to built the house.
    """
    turtle.down()
    turtle.forward(wallSize)
    turtle.left(90)
    turtle.forward(wallSize)
    maxX = turtle.xcor()
    turtle.left(45)
    turtle.forward(wallSize / math.sqrt(2))
    maxY = turtle.ycor()
    turtle.left(90)
    turtle.forward(wallSize / math.sqrt(2))
    turtle.left(45)
    turtle.forward(wallSize)
    turtle.left(90)
    turtle.forward(wallSize)
    turtle.up()
    return 2 * (wallSize + wallSize / math.sqrt(2))

def spaceBetween(treenumber,totaltree):

    """
    This is the function for drawing ground between two
    things which takes treenumber and totaltree as input.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (100,0), heading (north), up
    :return: None
    """
    turtle.down()
    if treenumber < totaltree:
        turtle.forward(100)
    turtle.penup()


def drawTrees (type_of_tree):
    """
    Draws the tree based on type_of_tree.
    where we have tree type as 1 for Pine
    tree type as 2 for Maple
    and tree type as 3 for new type named MyTree
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: size of trunk and height of tree
    """
    if type_of_tree == 1:
        trunk = random.randint(50, 200)
        height = drawPine(trunk)

    elif type_of_tree == 2:
        trunk = random.randint(50, 150)
        height = drawMaple(trunk)

    else:
        trunk = random.randint(50, 100)
        height = drawMyTree(trunk)

    return trunk,height


def drawMyTree(trunk):
    """
    Draws the tree of type MyTree
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: height of tree
    """
    drawTrunk(trunk)
    turtle.right(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(30)
    turtle.right(60)
    turtle.forward(trunk)
    turtle.left(90)
    height = trunk + (30 * (3 ** .5) + 60)
    return height

def drawMaple(trunk):
    """
    Draws the tree of type Maple
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: height of tree
    """
    drawTrunk(trunk)
    turtle.penup()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()
    turtle.back(trunk+40)
    turtle.right(90)
    turtle.back(40)
    turtle.pendown()
    height = trunk + 80
    return height


def drawPine(trunk):
    """
    Draws the tree of type Pine
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: height of tree
    """
    drawTrunk(trunk)
    turtle.left(90)
    turtle.forward(35)
    turtle.right(120)
    turtle.forward(70)
    turtle.right(120)
    turtle.forward(70)
    turtle.right(120)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(trunk)
    turtle.left(90)
    height = trunk + (3**.5)*35
    return height

def drawTrunk(trunk):
    """
    Draws the trunk of the tree
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,trunk), heading (north), up
    :return: None
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(trunk)

def calculate_wall_size(total_wood):
    """
    calculates new wall size depending upon availability
    of timber (addition of trunk of all trees)
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: new wall size
    """
    return total_wood / (2 + math.sqrt(2))

def draw_sun(ycor):
    """
    Draws the sun above given givin y-cordinate
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), right
    :return: None
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(3 * ycor / 2)
    turtle.down()
    turtle.circle(ycor/3)
    turtle.up


if __name__ == '__main__':
    init()
