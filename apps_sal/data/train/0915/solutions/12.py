t = int(input())

while(t):
    n = int(input())
    lt = input().split()
    for i in range(n):
        lt[i] = int(lt[i])
    new = set(lt)
    size = len(new)
    print(size)
    t = t - 1
