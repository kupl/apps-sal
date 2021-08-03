n = int(input())
a = [0] * 7
for k in range(0, n):
    s = input()
    for i in range(7):
        if s[i] == '1':
            a[i] += 1
print(max(a))
