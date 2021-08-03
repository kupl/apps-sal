s = input()
n = len(s)
sett = {}

for i in range(n):
    if s[i] not in sett:
        sett[s[i]] = []
    sett[s[i]].append(s[i + 1:] + s[:i])
ans = 0

# ao fazer sett.items(), é realizado unpack da chave,valor para k,l, respectivamente
for k, l in list(sett.items()):
    tmp = 0
    for j in range(n - 1):

        seen, sett1 = set(), set()

        for i in range(len(l)):

            if l[i][j] in sett1:
                sett1.remove(l[i][j])
            elif l[i][j] not in seen:
                sett1.add(l[i][j])
                seen.add(l[i][j])

        tmp = max(tmp, len(sett1))
    tmp /= n
    ans += tmp

# precisao 10^6
print('{:.7}'.format(ans))
