# cook your dish here
t = int(input())
while t:
    t -= 1
    a, b, c = list(map(int, input().split()))
    if (a > b and a < c) or (a > c and a < b):
        print(a)
    elif (b > a and b < c) or (b > c and b < a):
        print(b)
    elif (c > a and c < b) or (c > b and c < a):
        print(c)
    elif a == b or a == c:
        print(a)
    elif b == c:
        print(b)
