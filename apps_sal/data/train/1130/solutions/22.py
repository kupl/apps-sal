import math
n = int(input())
l = []
for i in range(n):
    N, D = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.append(D)
    lst.reverse()
    l.append(lst)


def number(li):
    d = li[0]
    li.remove(d)
    risk = []
    non_risk = []
    for i in li:
        if i >= 80 or i <= 9:
            risk.append(i)
        else:
            non_risk.append(i)
    return (math.ceil(len(risk) / d) + math.ceil(len(non_risk) / d))


for i in l:
    print(number(i))
