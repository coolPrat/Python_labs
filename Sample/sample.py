__author__ = 'Pratik'

import turtle

def drawSquare(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

def main():
    length = int(input('Enter side length: '))
    drawSquare(length)
    input('Hit enter to close...')

if __name__ == '__main__':
    main()
