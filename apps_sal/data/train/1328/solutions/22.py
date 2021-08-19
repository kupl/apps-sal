t = int(input())
while t:
    n = input().strip()
    c = 0
    for i in n:
        if i != '7' and i != '4':
            c += 1
    print(c)
    t -= 1
