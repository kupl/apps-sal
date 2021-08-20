for i in range(int(input())):
    N = int(input())
    l = list(map(int, input().split()))[:N]
    sum = l[N - 1] + l[N - 2]
    count = 0
    max = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] > max:
                max = l[i] + l[j]
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            s = l[i] + l[j]
            if s == max:
                count += 1
    f = N * (N - 1) / 2
    print(format(count / f, '.8f'))
