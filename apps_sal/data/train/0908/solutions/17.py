a = [1]


def lub(n):
    for i in range(len(a) - 1, -1, -1):
        if a[i] <= n:
            return str(i + 1)


for tc in range(int(input())):
    n = int(input())
    if n < a[len(a) - 1]:
        print(lub(n))
    else:
        while True:
            l = len(a) + 1
            a.append(l * (l + 1) / 2)
            if a[l - 1] > n:
                break
        print(lub(n))
