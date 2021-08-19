for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    q = int(input())
    s = ''
    for i in range(n):
        if lis[i] & 1 == 0:
            s += '0'
        else:
            s += '1'
    for _ in range(q):
        x = list(map(int, input().split()))
        l = x[0]
        r = x[1]
        temp = '1' * (r + 1 - l)
        if temp == s[l - 1:r]:
            print('ODD')
        else:
            print('EVEN')
