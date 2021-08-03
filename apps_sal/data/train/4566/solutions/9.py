
def counting_valleys(s):
    c = 0
    t = 0
    test = []
    for a in range(len(s)):
        if s[a] == "F":
            test.append(t)
        elif s[a] == "U":
            test.append(t + 1)
            t += 1
        else:
            test.append(t - 1)
            t -= 1
    for a in range(len(test) - 1):
        if test[a] == -1 and test[a + 1] == 0:
            c += 1
    return c

    pass
