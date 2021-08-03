grp = int(input())
tab = [""] * grp
for _ in range(grp):
    tab[_] = input()
m = 0
for i in range(7):
    t = 0
    for seq in tab:
        t += int(seq[i])
    if t > m:
        m = t
    if t == grp:
        break
print(m)
