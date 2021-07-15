l = []
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    l.append((a, b))

for i in l:
    for j in l:
        if i[0] + i[1] == j[0] and j[0] + j[1] == i[0]:
            print("YES")
            return
print("NO")

