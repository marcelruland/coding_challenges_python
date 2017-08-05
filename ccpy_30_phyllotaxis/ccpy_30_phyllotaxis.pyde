"""
Processing Python Mode implementation of Daniel Shiffman's 30th coding challenge
"Phyllotaxis"
github.com/CodingTrain/Rainbow-Code/tree/master/CodingChallenges/CC_30_Phyllotaxis
www.youtube.com/watch?v=KWoJgHFYWxY

Created on Saturday Aug 5 2017
@author: Marcel Ruland
"""
n = 0
c = 4
def setup():
    size(400, 400)
    colorMode(HSB)
    background(0)


def draw():
    global n, c
    a = n * radians(137.5)
    r = c * sqrt(n)
    x = r * cos(a) + width/2
    y = r * sin(a) + height/2

    fill(a % 255, 255, 255)
    noStroke()
    ellipse(x, y, 4, 4)

    n += 1
