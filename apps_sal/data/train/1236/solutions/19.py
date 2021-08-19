# cook your dish here
for t in range(int(input())):
    n = int(input())
    a = list(input())
    count = 0
    j = 1
    for i in range(0, n - 1):
        if a[i] == a[j]:
            j += 1
            count += 1
            pass
        else:
            j += 1
    print(count)
