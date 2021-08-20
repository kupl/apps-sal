def solve(s):
    if len(s) % 2:
        return -1
    height = 0
    counter = 0
    for x in s:
        if x == '(':
            height += 1
        else:
            height -= 1
        if height < 0:
            counter += 1
            height += 2
    return counter + height // 2
