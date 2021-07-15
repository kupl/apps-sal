def solve(s):
    numbers="0123456789"
    num = []
    str = ""
    for i in s:
        if i in numbers:
            str += i
        elif str != "":
            num.append(str)
            str = ""
    if str != "":
        num.append(str)
    return max([int(i) for i in num])
