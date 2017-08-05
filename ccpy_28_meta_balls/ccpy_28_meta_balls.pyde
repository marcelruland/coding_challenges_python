"""
Processing Python Mode implementation of Daniel Shiffman's 28th coding challenge
"Meta Balls"
github.com/CodingTrain/Rainbow-Code/tree/master/CodingChallenges/CC_28_MetaBalls
www.youtube.com/watch?v=ccYLb7cLB1I

Created on Friday Aug 4 2017
@author: Marcel Ruland
"""

def setup():
    global blobs
    size(200, 150)
    colorMode(HSB)
    blobs = [0] * 5
    for i in range(len(blobs)):
        blobs[i] = Blob(random(width), random(height))

class Blob:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.r = width/10
        self.vel = PVector.random2D()
        self.vel.mult(random(2, 5))

    def update(self):
        self.pos.add(self.vel)
        if self.pos.x > width or self.pos.x < 0:
            self.vel.x *= -1
        if self.pos.y > height or self.pos.y < 0:
            self.vel.y *= -1

    def show(self):
        noFill()
        stroke(0)
        strokeWeight(4)
        ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)



def draw():
    background(51)
    loadPixels()
    global blobs
    for x in range(width):
        for y in range(height):
            index = x + y * width
            sum = 0
            for i in range(len(blobs)):
                d = dist(x, y, blobs[i].pos.x, blobs[i].pos.y)
                if d > 0:
                    sum += width / 2 * blobs[i].r / d
                pixels[index] = color(sum, 255, 255)
    updatePixels()
    for i in range(len(blobs)):
        blobs[i].update()
        # blobs[i].show()
