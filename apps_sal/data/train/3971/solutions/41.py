def tidyNumber(n):
    count = 0
    play = str(n)
    for i in range(1,len(play)):
        if int(play[i])>=int(play[i-1]):
            count += 1
    return count == len(play)-1
