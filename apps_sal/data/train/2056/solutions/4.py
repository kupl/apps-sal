n = int(input())
a = list(input())
b = list(input())

count = 0
skip_next = False
for idx in range(n - 1):
    if skip_next:
        skip_next = False
        continue
    if a[idx] != b[idx] and a[idx] == b[idx + 1] and a[idx + 1] == b[idx]:
        count += 1
        a[idx] = b[idx]
        a[idx + 1] = b[idx + 1]
        skip_next = True

for idx in range(n):
    if a[idx] != b[idx]:
        count += 1

print(count)
