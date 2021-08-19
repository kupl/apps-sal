t = int(input())
for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()]
    b = [int(k) for k in input().split()]
    m = max(a)
    a = sum(a) - m
    z = max(b)
    b = sum(b) - z
    if a < b:
        print('Alice')
    elif a > b:
        print('Bob')
    else:
        print('Draw')
