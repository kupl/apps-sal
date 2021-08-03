t = int(input())
while(t > 0):
    t -= 1
    n, p = [int(x) for x in input().split()]
    if(p <= 2):
        print('impossible')
        continue
    else:
        s = 'a' + ('b' * (p - 2)) + 'a'
        s = s * int(n / p)
        print(s)
