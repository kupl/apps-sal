n = int(input())
t = list(map(int, input().split()))

sw = 0

while t != []:
    pr = 1 + t[1:].index(t[0])
    sw += pr - 1
    t = t[1:pr] + t[pr + 1:]

print(sw)
