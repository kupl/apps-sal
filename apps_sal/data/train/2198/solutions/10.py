n = int(input())

g = set()

for _ in range(n):
    s = input()
    while (True):
        new_s = s.replace('oo', 'u').replace('kh', 'h').replace('ou', 'uo')
        if new_s == s:
            break
        s = new_s

    if s not in g:
        g.add(s)

print(len(g))
