candidates = ((sq, str(sq)) for sq in (i * i for i in range(12, 3000)))
candidates = ((sq, s) for sq, s in candidates if '0' not in s)

d = {}  # 144: [144, 441], 256: [256, 625], ...
sqs = {}  # 144: [144, 441], 256: [256, 625], 441: [144, 441], 625: [256, 625], ...
for sq, s in candidates:
    sqs[sq] = d.setdefault(int(''.join(sorted(s))), [])
    sqs[sq].append(sq)


def next_perfectsq_perm(lower_limit, k):
    return sqs[min(x for x in sqs if x > lower_limit and len(sqs[x]) == k)][-1]
