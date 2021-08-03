# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    for i in range(n - 1):
        if l[i] % 2 == 0:
            for j in range(i + 1, n):
                if l[j] % 2 != 0:
                    count += 1
    print(count)
