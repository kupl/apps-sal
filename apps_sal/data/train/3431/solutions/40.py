def warn_the_sheep(queue):
    queue = queue[::-1]
    
    for i in range(0,len(queue)):
        if queue[i]=="wolf":
            if i==0:
                return "Pls go away and stop eating my sheep"
            else:
                return f"Oi! Sheep number {i}! You are about to be eaten by a wolf!"
        else:
            pass
