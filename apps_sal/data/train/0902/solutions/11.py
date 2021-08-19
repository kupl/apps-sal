t = int(input())
for _ in range(t):
    (n, s) = list(map(str, input().split()))
    n = int(n)
    (count1, count2) = (0, 0)
    for i in range(n):
        k = input()
        if k[0] == '0':
            count1 += k.count('0')
        elif k[0] == '1':
            count2 += k.count('1')
    if count1 == count2:
        if s == 'Dee':
            print('Dum')
        else:
            print('Dee')
    elif count1 > count2:
        print('Dee')
    else:
        print('Dum')
