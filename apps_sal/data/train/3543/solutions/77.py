def increment_string(string):
    l = 0
    for x in range(1, 100):
        if not string[-x:].isnumeric():
            l = x
            break
    if l == 1:
        return string + '1'
    else:
        num = string[-x + 1:]
        lenNum = len(num)
        num = int(num) + 1
        return string[:-x + 1] + str(num).zfill(lenNum)
