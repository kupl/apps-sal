t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    d1 = pow(pow(a[0], 2) + pow(a[1], 2), 0.5)
    d2 = pow(pow(a[2], 2) + pow(a[3], 2), 0.5)
    if(d1 > d2):
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")
