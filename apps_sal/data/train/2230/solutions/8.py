n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tog = [(p[i], a[i], b[i]) for i in range(0, n)]
tog.sort()
arr = [None, [], [], []]
us = [None, [], [], []]
link = []
for i in range(0, n):
    if tog[i][1] == tog[i][2]:
        arr[tog[i][1]].append(i)
        us[tog[i][1]].append(True)
        link.append([(tog[i][1], len(arr[tog[i][1]]) - 1)])
    else:
        arr[tog[i][1]].append(i)
        us[tog[i][1]].append(True)
        arr[tog[i][2]].append(i)
        us[tog[i][2]].append(True)
        link.append([(tog[i][1], len(arr[tog[i][1]]) - 1), (tog[i][2], len(arr[tog[i][2]]) - 1)])
ptr = [None, 0, 0, 0]
m = int(input())
buy = list(map(int, input().split()))
out = []
for c in buy:
    while ptr[c] < len(us[c]) and (not us[c][ptr[c]]):
        ptr[c] += 1
    if ptr[c] >= len(arr[c]):
        out.append(-1)
    else:
        v = arr[c][ptr[c]]
        us[c][ptr[c]] = False
        out.append(tog[v][0])
        for (cc, pp) in link[v]:
            us[cc][pp] = False
print(' '.join(map(str, out)))
