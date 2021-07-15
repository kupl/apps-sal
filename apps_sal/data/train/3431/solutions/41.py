def warn_the_sheep(queue):
    wolfpos = queue.index("wolf")
    sheepeat = len(queue) - queue.index("wolf") -1
    n = str(sheepeat)
    if n == "0":
        return("Pls go away and stop eating my sheep")
    else:
        return ("Oi! Sheep number "+n+"! You are about to be eaten by a wolf!")
