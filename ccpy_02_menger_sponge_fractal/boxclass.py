class Box(object):

    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.pos = PVector(self.x, self.y, self.z)

    def generate(self):
        boxes = []
        newR = 0.0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    sum = abs(x) + abs(y) + abs(z)
                    new_r = self.r / 3
                    if sum > 1: # change > to <= for a different, imo cooler, fractal
                        b = Box(self.pos.x + x * new_r, self.pos.y + y * new_r,self.pos.z + z * new_r, new_r)
                        boxes.append(b)
        return boxes

    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        noStroke()
        fill(255)
        box(self.r)
        popMatrix()
