n = int(input())
arr = [int(x) for x in input().split()]

i = 0
l = []
while i < n - 1:
    if arr[i] < arr[i + 1]:
        i = i + 1
    else:
        j = i + 1
        while j < n and arr[j] < arr[j - 1]:
            j = j + 1
        l.append((i, j - 1))
        i = j
if len(l) == 1:
    ll = []
    for i in range(l[0][1] + 1, l[0][0], -1):
        ll.append(i)

    if ll == arr[l[0][0]:l[0][1] + 1]:
        print(l[0][0] + 1, l[0][1] + 1)
    else:
        print(0, 0)
else:
    print(0, 0)
