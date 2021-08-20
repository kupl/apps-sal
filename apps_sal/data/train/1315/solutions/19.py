n = int(input())
l = []
for i in range(n):
    (a, b, c) = list(map(int, input().split()))
    t = [a, b, c]
    l.append(sorted(t))
l.sort()
l1 = []
for i in l:
    l1.append(l.count(i))
counter = 0
for i in l1:
    if i == 1:
        counter += 1
print(counter)
