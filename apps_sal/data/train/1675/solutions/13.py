from math import sqrt


def dis(a, b):
    return(sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2))


for i in range(int(input())):
    input()
    n = int(input())
    li = []
    for i in range(n):
        a, b = (int(i) for i in input().split())
        li.append((a, b))
    li = sorted(li, key=lambda x: (x[0], -x[1]))
    d = 0
    for i in range(0, n - 1):
        d += dis(li[i], li[i + 1])
    print(f'{d:.2f}')
