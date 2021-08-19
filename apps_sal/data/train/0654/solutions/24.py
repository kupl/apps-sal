# cook your dish here
t = int(input())
while t > 0:
    a, b, c = map(int, input().split())
    l = [a, b, c]
    l.sort()
    print(l[1])
    t -= 1
