t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.remove(max(a))
    b.remove(max(b))
    a1 = sum(a)
    b1 = sum(b)
    if a1 > b1:
        print('Bob')
    elif b1 > a1:
        print('Alice')
    else:
        print('Draw')
