p = [2]
for i in range(3, 1000, 2):
    if all((i % j for j in p)):
        p.append(i)


def prime_primes(N):
    cnt = 0
    sm = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[j] >= N:
                break
            cnt += 1
            sm += p[i] / p[j]
        if p[i] >= N:
            break
    return (cnt, int(sm))
