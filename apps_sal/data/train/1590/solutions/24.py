t = int(input())
for i in range(t):
    a = [int(i) for i in input().split()]
    a = sorted(a)
    if a[2] > a[0] + a[1]:
        print("No")
    else:
        print("Yes")
