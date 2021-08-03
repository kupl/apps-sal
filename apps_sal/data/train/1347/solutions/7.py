n, m = list(map(int, input().split()))
special = list(map(int, input().split()))
arr1 = []
arr2 = []
for i in range(m):
    f, p, s = list(map(str, input().split()))
    f, p = int(f), int(p)
    if f in special:
        arr1.append([f, p, s])
    else:
        arr2.append([f, p, s])
arr1 = sorted(arr1, key=lambda x: x[1])
arr2 = sorted(arr2, key=lambda x: x[1])
arr1.reverse()
arr2.reverse()
for i in range(len(arr1)):
    print(arr1[i][2])
for i in range(len(arr2)):
    print(arr2[i][2])
