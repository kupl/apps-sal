t = int(input())
while t > 0:
    a = list(map(int, input().split()))
    total_hours = 5 * 24
    p = a[len(a) - 1]
    sum = 0
    a.remove(p)
    for i in a:
        sum = sum + p * i
    if sum > total_hours:
        print('Yes')
    elif sum <= total_hours:
        print('No')
    t -= 1
