import sys
#f = sys.stdin
# f = open("input.txt", "r")
n = int(input())
a, b = [[],[]], [[],[]]
for i in range(n):
    t, xi, yi = map(int, input().split())
    if t == 1:
        a[0].append(xi)
        a[1].append(yi)
    else:
        b[0].append(xi)
        b[1].append(yi)
if sum(a[0]) >= sum(a[1]):
    print("LIVE")
else:
    print("DEAD")
if sum(b[0]) >= sum(b[1]):
    print("LIVE")
else:
    print("DEAD")
