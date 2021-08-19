# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    if n % 10 == 0:
        print(0)
    elif n % 5 == 0:
        print(1)
    else:
        print(-1)
