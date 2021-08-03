b = 1500000
lp = [0] * (b + 1)
pr = []
for i in range(2, b + 1):
    if not lp[i]:
        lp[i] = i
        pr.append(i)
    j = 0
    while j < len(pr) and pr[j] <= lp[i] and i * pr[j] <= b:
        lp[i * pr[j]] = pr[j]
        j += 1
pr.append(10000139)
pr.append(10000141)


def gap(g, start, stop):
    for i in range(len(pr) - 1):
        if pr[i] + g > stop:
            break
        if start <= pr[i] <= stop and pr[i] + g <= stop:
            if pr[i + 1] - pr[i] == g:
                return [pr[i], pr[i + 1]]
    return None
