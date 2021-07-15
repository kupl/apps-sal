def find_the_ball(k, li):
    for i in li:
        if k in i : k = [i[0],i[1]][i[0]==k]
    return k
