def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = [(sum(list(map(int, input().split()))), -i) for i in range(n)]
a.sort(reverse=True)

for i in range(n):
    if a[i][1] == 0:
        print(i + 1)
