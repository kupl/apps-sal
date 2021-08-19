a = int(input())
l = []
for i in range(1, 81):
    s = 0
    for j in range(len(str(abs(a - i)))):
        s = s + int(str(abs(a - i))[j])
    if s == i:
        l.append(a - i)
l.sort()
print(len(l))
for i in range(len(l)):
    print(l[i])
