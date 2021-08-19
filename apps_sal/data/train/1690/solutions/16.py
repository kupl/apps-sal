def is_relative(a, b):
    global K
    if len(a.intersection(b)) >= K:
        return True
    else:
        return False


def getval():
    (waste, *v) = map(int, input().split())
    return set(v)


(N, K) = map(int, input().split())
p = getval()
citizens = []
rel = []
for _ in range(N - 1):
    citizens.append(getval())
for citizen in citizens:
    if is_relative(p, citizen):
        rel.append(citizen)
        citizens.remove(citizen)
for relative in rel:
    for citizen in citizens:
        if is_relative(relative, citizen):
            rel.append(citizen)
            citizens.remove(citizen)
print(len(rel) + 1)
