def solve(s):
    highest = 0
    temp = ''
    for char in s:
        if char.isnumeric():
            temp += char
        else:
            if temp != '' and int(temp) >= highest:
                highest = int(temp)
            temp = ''
    return highest if temp == '' or highest > int(temp) else int(temp)
