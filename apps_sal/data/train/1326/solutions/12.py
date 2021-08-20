n = int(input())
li = []
for i in range(n):
    N = int(input())
    l = list(map(int, input().split()))
    li.append(l)


def dist(lst):
    ptr = lst[0]
    dst = 1
    for i in range(1, len(lst)):
        if ptr >= 1:
            ptr -= 1
            ptr += lst[i]
            dst += 1
        elif ptr == 0:
            break
    dst += ptr
    return dst


for k in li:
    print(dist(k) - 1)
