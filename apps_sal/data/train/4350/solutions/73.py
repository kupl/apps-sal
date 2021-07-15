def pre_fizz(n):
    list = []
    for i in range(n+1):
        list.append(i)
    list.pop(0)
    return list
