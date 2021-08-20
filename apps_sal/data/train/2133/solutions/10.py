n = int(input())
a = [0] * 7
for i in range(n):
    b = input()
    for j in range(7):
        a[j] += int(b[j])
print(max(a))
