t = int(input())

while(t):
    t -= 1

    n = int(input())

    a = list(map(int, input().split()))

    odd, even = 0, 0

    fo, fe = -1, -1
    for i in range(n):
        if (a[i] % 2 == 1):
            fo = i
            break

    for i in range(n):
        if(a[i] % 2 == 0):
            fe = i
            break

    for i in range(n):
        if i != fo:
            if (a[i] % 2 == 1):
                odd += 2
            else:
                odd += 1

    for i in range(n):
        if i != fe:
            if (a[i] % 2 == 1):
                even += 1
            else:
                even += 2

    print(min(odd, even))
