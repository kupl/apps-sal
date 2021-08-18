tests = int(input())

for test in range(tests):
    N = int(input())

    a = []
    for row in range(N):
        a.append([int(x) for x in input().split()])

    max_a = []
    for i in range(N):
        max_c = 0
        count = i
        for j in range(N - i):
            if count < N:
                max_c += a[j][count]
            count += 1

        max_a.append(max_c)

    for i in range(N):
        if i == 0:
            continue

        max_c = 0
        count = i
        for j in range(N - i):
            if count < N:
                max_c += a[count][j]
            count += 1
        max_a.append(max_c)

    print(max(max_a))
