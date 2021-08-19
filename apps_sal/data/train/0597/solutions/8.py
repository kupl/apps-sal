# cook your dish here
for i in range(int(input())):
    n = int(input())
    arr1 = []
    arr2 = []
    for i in range(n):
        l = input().split()
        arr1.append(int(l[0]))
        arr2.append(int(l[1]))
    arr1.append(arr1[-1])
    arr1.insert(0, arr1[0])
    arr2.sort()
    base = []
    for i in range(1, n + 1):
        base.append(arr1[i + 1] - arr1[i - 1])
    base.sort()
    ans = 0
    for i in range(n):
        ans += base[i] * arr2[i]
    print(ans)
