t = 0
for i in range(0, int(input())):
    a = list(map(int, input().split()))
    if a.count(1) >= 2:
        t += 1
print(t)
