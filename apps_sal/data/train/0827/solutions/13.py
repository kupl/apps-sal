for i in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ac = 0
    bc = 0
    t = 0
    for i in range(n):
        if (s[i] == 'a'):
            ac += 1
        if(s[i] == 'b'):
            bc += 1
            t += ac
    r = k * t
    r += k * (k - 1) // 2 * ac * bc
    print(r)
