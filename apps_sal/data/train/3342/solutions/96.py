def pattern(n):
    char = 1
    nTimes = 1
    string = ''
    while nTimes <= n:
        for i in range(0, nTimes):
            string += str(char)
        string += '\n'
        nTimes += 1
        char += 1
    return string[0:len(string) - 1]
