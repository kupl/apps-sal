def warn_the_sheep(queue):
    count=0
    for i in range(len(queue)-1,-1,-1):
        if queue[i]=="wolf" and count!=0: return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(count)
        count+=1
    return "Pls go away and stop eating my sheep"
