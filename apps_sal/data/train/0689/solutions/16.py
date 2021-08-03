t = int(input())
lst = []
lst2 = []
stat = False
for x in range(t):
    lst.append(list(map(int, input().split())))
for j in range(len(lst)):
    for i in range(len(lst)):
        if i == j:
            continue
        if j == lst[-1]:
            break
        if sum(lst[j]) == lst[i][0] and sum(lst[i]) == lst[j][0]:
            stat = True
            break
if stat:
    print("YES")
else:
    print("NO")
