def find_digit(num, nth):
    #your code here
    strnum = str(num)
    if nth <= 0:
        return -1
    elif nth > len(strnum):
        return 0
    else:
        return int(strnum[len(strnum)-nth])
