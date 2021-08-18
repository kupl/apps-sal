t = int(input())
lst1 = []
lst = []
for i in range(t):

    a, b = list(map(int, input().split()))
    lst.append((a, b))
for i in range(0, t):
    temp = lst[i][0] + lst[i][1]
    for j in lst:
        if j != lst[i] and j[0] == temp:
            temp1 = j[0] + j[1]
            if temp1 == lst[i][0]:
                lst1.append(1)
                break
            break
if len(lst1) == 0:
    print("NO")
else:
    print("YES")
