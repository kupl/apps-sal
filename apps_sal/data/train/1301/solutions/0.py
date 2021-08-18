n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
for i in l:
    b = list(map(int, str(i)))
    b.sort(reverse=True)
    s = [str(i) for i in b]
    r = int("".join(s))
    print(r)
