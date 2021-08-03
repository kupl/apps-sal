for _ in range(int(input())):
    n = int(input())
    l = [int(j) for j in input().split()]
    count = 1
    for i in range(1, n):
        if i - 5 < 0:
            mini = min(l[0: i])
            if mini > l[i]:
                count += 1
        else:
            mini = min(l[i - 5: i])
            if mini > l[i]:
                count += 1
    print(count)
