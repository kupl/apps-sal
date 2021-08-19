n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
i = 0
while len(a) != 0 and len(a) != 1:
    if a[i] == a[i + 1]:
        a.pop(0)
        a.pop(0)
    else:
        a.pop(0)
    count += 1
if len(a) == 1:
    count += 1
print(count)
