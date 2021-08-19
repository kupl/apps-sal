t = int(input())
for i in range(t):
    (n, m) = map(int, input().split())
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    s1 = set(arr1)
    s2 = set(arr2)
    l = []
    for i in arr1:
        if i not in s2:
            l.append(i)
    for i in arr2:
        if i not in s1:
            l.append(i)
    l.sort()
    print(*l)
