def solve(s):
    lst = [0, 0, 0, 0]
    for char in s:
        if char.isupper():
            lst[0] += 1
        elif char.islower():
            lst[1] += 1
        elif char.isdigit():
            lst[2] += 1
        else:
            lst[3] += 1
    return lst
