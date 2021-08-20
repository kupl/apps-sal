t = int(input())
for i in range(t):
    (v, w) = map(int, input().strip().split())
    count = 1
    if w > v:
        w = v
    count = count + w
    print(count)
