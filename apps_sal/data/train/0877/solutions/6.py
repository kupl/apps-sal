# cook your dish here
for _ in range(int(input())):
    x, y, k, n = list(map(int, input().split()))
    diff = abs(x - y)
    if (diff % (2 * k)) == 0:
        print("Yes")
    else:
        print("No")
