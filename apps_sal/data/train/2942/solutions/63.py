def fold_to(distance):
    epais = 0.0001
    compte=0
    if distance<0:
        return None
    else:
        while epais<distance:
            epais=epais*2
            compte += 1
        return compte
