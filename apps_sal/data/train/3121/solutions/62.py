def solve(ar):
    x = len(ar)
    i = 0
    temp = 0
    while i < x:
        c = 0
        char = ar[i]
        while c <= x - 1:
            if char == -ar[c]:
                i += 1
                break
            c += 1
        else:
            temp = char
            return temp
    return temp
