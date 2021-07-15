def seven(m):
    turns = 1
    print(m)
    if m == 0:
        return(0, 0)
    num = int(str(m)[:-1]) - int(str(m)[-1]) * 2
    while num >= 100 :
        print(num)
        num = int(str(num)[:-1]) - int(str(num)[-1]) * 2
        turns += 1
    return(num, turns)
