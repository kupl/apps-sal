n, l = [int(x) for x in input().split()]
s = []
for i in range(n):
    s.append(input())
s.sort()

print("".join(s))
