def luck_check(string):
    lsum = 0
    rsum = 0
    i = 0
    j = len(string) - 1
    while i < j:
        lsum += int(string[i])
        rsum += int(string[j])
        i += 1
        j -= 1
    return lsum == rsum
