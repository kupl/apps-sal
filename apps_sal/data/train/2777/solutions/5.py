def solve(st):
    tempstr = ''
    for i in reversed(st):
        if i.isalpha():
            tempstr += i
        if i.isdigit():
            tempstr = tempstr * int(i)
    return tempstr[::-1]
