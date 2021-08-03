p, s = map(int, input().split())
diff = list()
for i in range(s):
    diff.append([])
for i in range(p):
    n = 0
    c = list(map(int, input().split()))
    sc = list(map(int, input().split()))
    dictionary = dict(zip(c, sc))
    c.sort()
    for j in range(s - 1):
        if dictionary[c[j]] > dictionary[c[j + 1]]:
            n += 1
    diff[n].append(i + 1)
for i in range(s):
    for j in range(len(diff[i])):
        print(diff[i][j])
