for i in range(int(input())):
    n, k = map(int, input().split())
    l = input().split()
    s = 0
    for j in range(len(l)):
        if j % 2 == 0 and l[j] == '1':
            if s >= 0:
                s += 1
            else:
                s -= 1
        elif l[j] == '1':
            if s >= 0:
                s -= 1
            else:
                s += 1
    if abs(s) >= k:
        print(1)
    else:
        print(2)
