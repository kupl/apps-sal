# cook your dish here
n = int(input())
while n > 0:
    a = list(map(int, input().strip().split()))
    a.sort()
    print(a[1])
    n = n - 1
