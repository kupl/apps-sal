# cook your dish here
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if i % 2 == 0:
            if s > 0:
                s += l[i]
            else:
                s -= l[i]
        else:
            if s > 0:
                s -= l[i]
            else:
                s += l[i]
    if abs(s) >= k:
        print('1')
    else:
        print('2')
