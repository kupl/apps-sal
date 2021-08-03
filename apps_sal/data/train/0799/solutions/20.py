# cook your dish here
c = 0
for _ in range(int(input())):
    l = list(map(int, input().split()))
    if l.count(1) >= 2:
        c += 1
print(c)
