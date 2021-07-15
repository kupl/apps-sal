def stringy(size):
    n = int(size / 2)
    i = 0
    c = "10"
    output = ""
    for i in range(n):
        output = output + c
        i += 1
    if size%2 == 1:
        output = output + "1"

    return output
