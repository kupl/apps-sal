s = input()

if s[0] == '0' or s[-1] == '1' or s[:-1] != s[:-1][::-1]:
    print((-1))
    return

edges = []
head = 0
for idx, i in enumerate(s[:-1]):
    edges.append([head, idx + 1])
    if i == '1':
        head = idx + 1
for i, j in edges:
    print((i + 1, j + 1))
