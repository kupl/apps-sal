s = input()
n = int(input())
data = []
for i in range(n):
    data.append(input())
mark = 0
for i in range(n):
    for j in range(n):
        if s in (data[i] + data[j]):
            mark = 1

if mark:
    print("YES")
else:
    print("NO")
