n, k, p = list(map(int, input().strip().split()))
list1 = list(map(int, input().strip().split()))
list2 = sorted(list1)

map1 = dict()
curr = list2[0]
index = 0
for i in range(1, n):
    if list2[i] - list2[i - 1] > k:
        for j in range(index, i):
            map1[list2[j]] = list2[i - 1]
        curr = list2[i]
        index = i

for j in range(index, n):
    map1[list2[j]] = list2[n - 1]


for _ in range(p):
    a, b = list(map(int, input().strip().split()))
    pos1 = list1[a - 1]
    pos2 = list1[b - 1]
    start = min(pos1, pos2)
    end = max(pos1, pos2)

    if map1[start] >= end:
        print("Yes")
    else:
        print("No")
