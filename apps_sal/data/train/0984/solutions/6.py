# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    count = 0
    j = 0
    while (j < n):
        if a[j] % 2 == 0:
            i += 1
        else:
            count += i
        j += 1
    print(count)
