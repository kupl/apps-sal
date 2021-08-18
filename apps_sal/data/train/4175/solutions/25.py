def repeater(string, n):
    new = str()
    for i in range(1, n + 1):
        new = new + str(string)

    return new
