t = int(input())
for i in range(t):
    a = input().split(" ")
    n = int(a[0])
    m = int(a[1])
    if((n % m) % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
