try:
    m = int(input())
    l = list(map(int, input().split()))
    for _ in range(int(input())):
        n = int(input()) - 1
        print(l[n])
        del l[n]
except:
    pass
