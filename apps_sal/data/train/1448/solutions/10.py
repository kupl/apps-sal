# cook your dish here
for _ in range(int(input())):
    a, d, k, n, inc = map(int, input().split())
    sum = a
    for i in range(1, n):
        if i % k == 0:
            d = d + inc
        sum = sum + d
    print(sum)
