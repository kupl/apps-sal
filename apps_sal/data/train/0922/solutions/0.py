t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    hmap = {}
    for i in range(n):
        if arr1[i] in hmap:
            hmap[arr1[i]] += 1
        else:
            hmap[arr1[i]] = 1

    for i in range(m):
        if arr2[i] in hmap:
            hmap[arr2[i]] += 1
        else:
            hmap[arr2[i]] = 1
    ans = []
    # print(hmap)
    for key in hmap:
        if hmap[key] == 1:
            ans.append(key)
    ans.sort()
    for x in ans:
        print(x, end=' ')
    print()
