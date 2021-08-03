def solve(s):
    char = s.replace(" ", "")[::-1]
    list = s.split(" ")
    i = 0
    for x in list:
        list[i] = char[:len(x)]
        char = char[len(x):]
        i += 1
    return " ".join(list)
