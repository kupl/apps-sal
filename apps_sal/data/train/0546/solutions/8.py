def balls():
    d = int(input())
    i = 0
    while 1:
        if 2 ** i > d:
            i -= 1
            break
        i += 1
    temp = 0
    result = 0
    j = i
    while j >= 0:
        if temp + 2 ** j == d:
            return result
        if temp + 2 ** j > d:
            j -= 1
        else:
            temp += 2 ** j
            result += 1
    return result


t = int(input())
for loop in range(t):
    print(balls())
