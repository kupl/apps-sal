def solve(s):
    outl = []
    s += " "
    for el in s:
        if el.isdecimal():
            outl.append(el)
        else:
            outl.append(" ")

    temp = ''
    lis = []
    for i in range(len(outl) - 1):
        if outl[i].isdecimal():
            temp += outl[i]
            if outl[i + 1] == " ":
                lis.append(int(temp))
                temp = ""
    return max(lis)
