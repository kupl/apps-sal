a, b = map(int, input().split())
k = []
for _ in range(a + b):
    p = int(input())
    if p != -1:
        k.append(p)
    else:
        print(max(k))
        k.remove(max(k))
