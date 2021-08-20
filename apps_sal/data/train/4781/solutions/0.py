import math


def spider_to_fly(spider, fly):
    web = {'A': 0, 'B': 45, 'C': 90, 'D': 135, 'E': 180, 'F': 225, 'G': 270, 'H': 315}
    angle = min(abs(web[spider[0]] - web[fly[0]]), 360 - abs(web[spider[0]] - web[fly[0]]))
    (sideA, sideB) = (int(spider[1]), int(fly[1]))
    return math.sqrt(sideA ** 2 + sideB ** 2 - 2 * sideA * sideB * math.cos(angle * math.pi / 180))
