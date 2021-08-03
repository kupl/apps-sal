a = input()
b = sorted([int(i) for i in input().split()])[0]
c = int(input())
d = sorted([int(i) for i in input().split()])
p = 0
while len(d):
    for i in range(0, min(len(d), b)):
        p += d.pop()
    for i in range(0, min(len(d), 2)):
        a = d.pop()
print(p)
