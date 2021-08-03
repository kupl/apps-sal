def cupc(n):
    if(n == 2):
        return n
    else:
        return (n // 2) + 1


t = int(input())
for i in range(0, t):
    n = int(input())
    print(cupc(n))
