def find(sets, a):
    if a == sets[a]:
        return a
    sets[a] = find(sets, sets[a])
    return sets[a]


def join(sets, a, b):
    a = find(sets, a)
    b = find(sets, b)
    if a != b:
        sets[a] = b


n, m = (int(x) for x in input().split())
sets = list(range(n))
langs = []
for i in range(n):
    langs.append(set([int(x) for x in input().split()][1:]))
if all(len(lang) == 0 for lang in langs):
    print(n)
    return
for i in range(n):
    for lang in langs[i]:
        for j in range(i):
            if lang in langs[j]:
                join(sets, i, j)
print(len(set(find(sets, s) for s in sets)) - 1)
