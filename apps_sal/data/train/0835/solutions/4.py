t = int(input())
while t > 0:
    t -= 1
    m, n = list(map(int, input().split()))
    if m == 1 and n > 2:
        print('No')
        continue
    elif n == 1 and m > 2:
        print('No')
        continue
    if m % 2 == 0 or n % 2 == 0:
        print('Yes')
    elif m == 1 and n == 1:
        print('No')
    else:
        print('No')
