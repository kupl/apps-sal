for ad in range(int(input())):
    n = int(input())
    s = list(input())
    zero = s.count('0')
    one = s.count('1')
    l = s
    ans = 0
    for i in range(n):
        if l[i] == '0':
            zero -= 1
            ans += one
        else:
            one -= 1
            ans += zero
    print(ans)
