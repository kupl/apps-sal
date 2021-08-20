for _ in range(int(input())):
    n = input().strip()
    a = 0
    for i in n:
        if i != '4' and i != '7':
            a += 1
    print(a)
