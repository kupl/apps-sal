def counting_valleys(s):
    altitude = 0
    result = 0
    for c in s:
        if c == "U":
            altitude += 1
            if altitude == 0:
                result += 1
        elif c == "D":
            altitude -= 1
    return result
