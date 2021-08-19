# cook your dish here
k = int(input())

for j in range(0, k):
    n = int(input())
    a = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if i - 5 < 0:
            mini = min(a[0: i])
            if mini > a[i]:
                count += 1
        else:
            mini = min(a[i - 5: i])
            if mini > a[i]:
                count += 1
    print(count)
