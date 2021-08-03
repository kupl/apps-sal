# cook your dish here
t = int(input())
while t:
    a, b, c = [int(i) for i in input().split(' ')]
    k = (c - b) // a
    print((k * a) + b)
    t -= 1
