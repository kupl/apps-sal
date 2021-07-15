def warn_the_sheep(queue):
    position = 0 
    for i in range(len(queue)):
        if (queue[i]=="wolf"):
            position = len(queue)-1 -i
            break
    if (position == 0):
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number "+str(position)+"! You are about to be eaten by a wolf!"
