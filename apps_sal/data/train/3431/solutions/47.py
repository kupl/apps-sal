def warn_the_sheep(queue):
    db = 0
    for i in range(len(queue) - 1, -1, -1):
        if queue[i] == "wolf" and db == 0:
            return "Pls go away and stop eating my sheep"
        elif queue[i] == "wolf" and db != 0:
            return "Oi! Sheep number " + str(db) + "! You are about to be eaten by a wolf!"
        else:
            db = db + 1
