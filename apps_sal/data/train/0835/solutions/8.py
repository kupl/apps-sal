def checkval(m, n):
    if m == 1:
        if n == 2:
            return 1
        return 0
    if n == 1:
        if m == 2:
            return 1
        return 0
    if (not(n & 1) or not(m & 1)):
        return 1
    return 0


t = int(input())
while t:
    t -= 1
    n, m = input().split()
    n = int(n)
    m = int(m)
    if(checkval(m, n)):
        print("Yes")
    else:
        print("No")
