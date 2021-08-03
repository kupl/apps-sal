n = int(input())
for i in range(0, n):
    a, b = list(map(int, input().split()))
    l = list(map(int, input().split()))
    l = [i + b for i in l]
    count = 0
    for i in l:
        if i % 7 == 0:
            count += 1
    print(count)
