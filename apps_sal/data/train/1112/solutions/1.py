# cook your dish here

t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        count = 1
        while(n > 0):
            for j in range(1, n + 1):
                print(count, end="")
                count += 1
            n -= 1
            print()
