n = int(input())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort()
s = 0
i = n - 1
while i >= 0:
    x = 2 * l[i]
    if l[-1] >= x:
        j = i
        while j < len(l):
            if l[j] >= x:
                l.pop(j)
                l.pop(i)
                s += 1
                break
            j += 1
    i -= 1
s += len(l)
print(s)
