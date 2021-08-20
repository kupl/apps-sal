t = int(input())
while t > 0:
    t -= 1
    s = input()
    val = 0
    ctr = 0
    for i in s:
        if ctr == 6:
            ctr = 0
        elif i == 'M':
            val += 3
            ctr += 1
        else:
            val += 4
            ctr += 1
    print(val)
