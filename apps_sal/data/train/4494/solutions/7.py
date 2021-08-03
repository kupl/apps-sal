def points(games):
    sum = 0
    for g in games:
        s = g.split(':')
        if(s[0] > s[1]):
            sum += 3
        elif(s[0] == s[1]):
            sum += 1
    return(sum)
