N, L, *Ss = open(0).read().split()

ans = ""
for s in sorted(Ss):
    ans += s
print(ans)
