test = int(input())
for i in range(0, test):
    h, x = [int(x) for x in input().split()]
    if h >= x:
        print("Yes")
    else:
        print("No")
