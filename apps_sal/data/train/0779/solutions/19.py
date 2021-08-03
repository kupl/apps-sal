# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort(reverse=True)
    sum = (a[0] + a[1]) / 2
    # print(sum,a)
    for i in range(2, n):
        sum = (sum + a[i]) / 2
        # print(sum)
    print(sum)
