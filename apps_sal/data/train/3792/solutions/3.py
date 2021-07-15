def slogans(p,r):
    start = 0
    count = 0
    for i in range(1, len(r)):
        if r[start:i+1] not in p:
            count += 1
            start = i
    return count + 1
