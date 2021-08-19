# your code goes here
t = int(input())
for sc in range(t):
    n, m = list(map(int, input().split()))
    if n == 1 or m == 1:
        if n * m == 2:
            print("Yes")
        else:
            print("No")
    elif (n * m) % 2 == 0:
        print("Yes")
    else:
        print("No")
