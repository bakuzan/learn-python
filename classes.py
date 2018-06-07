
class Fish:

    def __init__(self, type):
        self.type = type
        self.moving = False

    def swim(self):
        self.moving = True
        print("{} is swimming".format(self.type))


f = Fish('goldfish')
g = Fish('great white')

f.swim()
print(f.__class__)
print(f.moving)

print(g.moving)
