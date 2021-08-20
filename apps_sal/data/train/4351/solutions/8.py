def find_middle(string):
    if type(string) != str:
        return -1
    result = 1
    count = 0
    for c in string:
        if c.isdigit():
            count += 1
            result *= int(c)
    if count:
        if len(str(result)) % 2 == 0:
            final = str(result)[len(str(result)) // 2 - 1:len(str(result)) // 2 + 1]
            if final[0] == '0':
                return int(final[1])
            else:
                return int(final)
        else:
            return int(str(result)[len(str(result)) // 2])
    else:
        return -1
