t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    li = []

    count = 0
    for i in l:
        if i in li:
            count += 2
            li = []
        else:
            li.append(i)

    print(n - count)
