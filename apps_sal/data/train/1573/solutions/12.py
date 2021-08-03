for t in range(int(input())):
    n = int(input())
    a = n * (n - 1) / 2
    if a % n == 0:
        print("YES")
        r = int(a / n)
        rem = n - r - 1
        l = '0' + '1' * r + '0' * rem
        for u in range(n):
            print(l)
            l = l[-1] + l[:-1]
    else:
        print("NO")
