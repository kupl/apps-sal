import math
def survivor(zombies):
    size = len(zombies)
    if size == 0:
        return -1
    if (1 in zombies):
        return 0

    gcd = zombies[0]
    for i in range(len(zombies) - 1):
        gcd = math.gcd(gcd, zombies[1 + i])
    if gcd != 1:
        return -1

    maxSize = (zombies[0] * zombies[1]) - zombies[0] - zombies[1]
    posible = [False for _ in range(maxSize + 1)]
    posible[0] = True


    for zombie in zombies:
        if zombie <= maxSize:
            for i in range(zombie, maxSize + 1):
                if not posible[i]:
                    posible[i] = posible[i - zombie]
    largest = 0
    for i in range(maxSize + 1):
        if not posible[i]:
            largest = i
    return largest
