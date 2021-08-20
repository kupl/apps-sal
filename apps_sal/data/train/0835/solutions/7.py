t = eval(input())
while t > 0:
    (a, b) = input().split(' ')
    a = int(a)
    b = int(b)
    t -= 1
    if a == 1 and b == 2:
        print('Yes')
        continue
    elif a == 2 and b == 1:
        print('Yes')
        continue
    elif a == 1 or b == 1:
        print('No')
        continue
    elif a % 2 == 0 or b % 2 == 0:
        print('Yes')
        continue
    else:
        print('No')
