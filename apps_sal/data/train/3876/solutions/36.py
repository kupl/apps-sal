def find(n):
    list_1 = []
    for x in range(1,n+1):
        if x%3 == 0 or x%5 == 0:
            list_1.append(x)
    i = 0
    for y in list_1:
        i = i+y
    return i
