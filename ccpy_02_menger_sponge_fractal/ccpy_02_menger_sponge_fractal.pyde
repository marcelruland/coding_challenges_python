"""
Processing Python Mode implementation of Daniel Shiffman's 2nd coding challenge
"Menger Sponge Fractal"
github.com/CodingTrain/Rainbow-Code/tree/master/CodingChallenges/CC_02_MengerSponge
www.youtube.com/watch?v=LG8ZK-rRkXo&t=5s

Created on Saturday Aug 5 2017
@author: Marcel Ruland
"""
from boxclass import *
a = 0
b = Box(0, 0, 0, 200.0)
sponge = []

def setup():
    global sponge
    size(400, 400, P3D)
    sponge.append(b)

def mousePressed():
    global sponge
    next = []
    for b in sponge:
        new_boxes = b.generate()
        next = next + new_boxes
    sponge = next

def draw():
    global a, b, sponge
    background(51)
    stroke(255)
    noFill()
    lights()

    translate(width / 2, height / 2)
    rotateX(a)
    rotateY(a * 0.4)
    rotateZ(a * 0.1)
    for b in sponge:
        b.show()
    a += 0.01