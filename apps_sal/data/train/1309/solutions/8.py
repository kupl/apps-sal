t = int(eval(input("")))
while(t != 0):
    k = int(eval(input("")))
    s = ''
    for i in range(k, 0, -1):
        for j in range(k, 0, -1):
            if i >= k and j == i:
                s = s + str(j)
                continue
            if i < k and j > i:
                s = s + '*'
            else:
                s = s + str(j)
        print(s)
        s = ''
    t -= 1
