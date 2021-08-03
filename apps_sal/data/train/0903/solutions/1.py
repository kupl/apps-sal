# cook you dish here
t = int(input())
l = []
for i in range(t):
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    x = (x1 * y2 + x2 * y1) / (y1 + y2)
    l.append(x)
for i in l:
    print(i)
