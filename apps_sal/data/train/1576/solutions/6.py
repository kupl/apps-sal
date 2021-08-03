for _ in range(int(input())):
    n = int(input())
    l = list(range(1, n + 1))
    for x in range(n):
        print(*l[x:], sep="", end="")
        print(*l[:x], sep="")
# cook your dish here
