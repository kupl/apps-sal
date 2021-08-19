t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n * 4)
    else:
        temp = n / 2 + 1
        if temp % 2 == 0:
            print(n)
        else:
            print(n * 2)
