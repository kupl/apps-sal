n = int(input())
a = [0] + list(map(int, input().split()))
ans = 0
for i in range(1, len(a)):
    if a[i] == -1:
        continue
    j = i
    while a[j] != -1:
        prev = j
        j = a[j]
        a[prev] = -1
    ans += 1
if n % 2 == 0:
    if ans % 2 == 0:
        print("Petr")
    else:
        print("Um_nik")
else:
    if ans % 2 == 0:
        print("Petr")
    else:
        print("Um_nik")
