t = int(input())
while(t > 0):
    t -= 1
    n, m = list(map(int, input().split()))
    if n % 2 != 0 and m % 2 != 0:
        print("No")
    elif m == 1 and n == 2:
        print("Yes")
    elif n == 1 and m == 2:
        print("Yes")
    elif m < 2 or n < 2:
        print("No")
    else:
        print("Yes")
