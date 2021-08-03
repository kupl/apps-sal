n = int(input())
for i in range(n):
    a, b, c = list(map(int, input().split()))
    if (a > b and b > c) or (c > b and b > a):
        print(b)
    elif (b > a and a > c) or (c > a and a > b):
        print(a)
    elif (b > c and c > a) or (a > c and c > b):
        print(c)
