c = 0
for _ in range(int(input())):
    lst, s = list(map(int, input().split())), 0
    for i in lst:
        s += i
    if s > 1:
        c += 1

print(c)
