m = int(input())
a = list(map(int, input().split()))
for i in range(int(input())):
    n = int(input())
    print(a[n - 1])
    a.remove(a[n - 1])
