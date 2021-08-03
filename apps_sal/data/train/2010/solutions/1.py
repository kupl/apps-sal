input()
l, r = [0], [0]
for a, b in (lambda a: list(zip(a, reversed(a))))([0] + list(map(int, input().split())) + [0]):
    l.append(min(a, l[-1] + 1))
    r.append(min(b, r[-1] + 1))
print(max(list(map(min, list(zip(l[1:], reversed(r[1:])))))))
