def hotpo(n):
    temp = [n]
    while True:
        if temp[-1] % 2 != 0:
            if temp[-1] == 1:
                return len(temp) - 1
            temp.append(3 * temp[-1] + 1)
        else:
            temp.append(temp[-1] / 2)

