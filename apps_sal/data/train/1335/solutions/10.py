n = int(input())
a = [int(i) for i in input().split()]
temp = set(a)
count = 0
for i in temp:
    t = a.count(i)
    if t % 2 == 0:
        count += int(t / 2)
    else:
        count += int(t / 2) + 1
print(count)
