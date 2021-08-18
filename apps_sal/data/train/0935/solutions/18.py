n = int(input())
for i in range(n):
    z = int(input())
    if z % 10 == 0:
        print("0")
    elif z % 5 == 0:
        print("1")
    else:
        print("-1")
