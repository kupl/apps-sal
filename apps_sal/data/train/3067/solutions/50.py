def getVolumeOfCubiod(length, width, height):
    cub = Cubiod(length, width, height)
    return cub.getVolume()


class Cubiod:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def getVolume(self):
        return self.length * self.width * self.height

    def getSA(self):
        return (self.length * self.height * 2) + (self.length * self.width * 2) + (self.height * self.width * 2)

    def speedProb(self):
        return 9.87 * min(self.length, self.width, self.height)

    def damage(self):
        return self.getVolume() * 1900 * self.speedProb()

    def velocity(self):
        return self.speedProb() ** 2

    def crimeLevel(self):
        return self.velocity() * self.damage() + self.getSA()
