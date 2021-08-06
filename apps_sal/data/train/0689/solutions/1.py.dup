# cook your dish here
t = int(input())
i = 0
a = 0
d = dict()
while i < t:
    l = input().split()
    d[int(l[0])] = int(l[0]) + int(l[1])
    i += 1
for k in d:
    if d[k] in d:
        if d[d[k]] == k:
            a = 1
            break
if a == 1:
    print("YES")
else:
    print("NO")
