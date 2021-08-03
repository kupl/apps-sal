def find_average(n):
    aver = 0
    for i in range(len(n) + 1):
        aver += i
    return int(aver / len(n))
