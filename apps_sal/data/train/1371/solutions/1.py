n = int(input())
for i in range(n):
    m, k = map(int, input().split())
    l = list(map(int, input().split()[:m]))
    count = 0
    for i in l:
        if (i + k) % 7 == 0:
            count += 1
    print(count)
