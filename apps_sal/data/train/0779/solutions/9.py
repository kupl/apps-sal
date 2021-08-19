# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    k = (a[0] + a[1]) / 2
    for i in range(2, n):
        k = (k + a[i]) / 2
    print(k)
