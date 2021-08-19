n = int(input())
list1 = []
list2 = []
for i in range(n):
    (a, h) = list(map(int, input().split()))
    list1.append(a)
    list2.append(h)
count = 2
for j in range(1, n - 1):
    k = list1[j] - list2[j]
    if k > list1[j - 1]:
        count += 1
    else:
        z = list1[j] + list2[j]
        if z < list1[j + 1]:
            count += 1
            list1[j] = list2[j] + list1[j]
if n == 1:
    print('1')
else:
    print(count)
