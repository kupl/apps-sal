3
n = int(input())
a = [True] * (n + 2)
for i in range(2, n + 2):
    if not a[i]:
        continue
    j = i * i
    while j < n + 2:
        a[j] = False
        j += i
if n <= 2:
    print(1)
else:
    print(2)
print(' '.join('1' if x else '2' for x in a[2:]))
