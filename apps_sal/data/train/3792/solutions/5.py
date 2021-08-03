def slogans(p, r):
    count, tmp = 0, ""
    for char in r:
        if tmp + char in p:
            tmp += char
        else:
            count += 1
            tmp = char
    return count + 1
