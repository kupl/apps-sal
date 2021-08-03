# cook your dish here
l = []
m = []
c = []
s, k = 0, 0
for i in range(int(input())):
    a, b = map(int, input().split(" "))
    s = s + a
    k = k + b
    l.append(s)
    m.append(k)
for j in range(len(l)):
    c.append(abs(l[j] - m[j]))
if(l[c.index(max(c))] > m[c.index(max(c))]):
    print("1", end=" ")
else:
    print("2", end=" ")
print(max(c))
