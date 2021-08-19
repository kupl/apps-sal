def bird(w):
    return {4: lambda w: w[0][:1] + w[1][:1] + w[2][:2] + w[3][:2], 3: lambda w: w[0][:2] + w[1][:2] + w[2][:2], 2: lambda w: w[0][:3] + w[1][:3], 1: lambda w: w[0][:6]}[len(w)](w)


def create_report(names):
    D = {}
    for (b, i) in [(bird(' '.join(s.split()[:-1]).upper().replace('-', ' ').split()), int(s.split()[-1])) for s in names]:
        D[b] = D.get(b, 0) + i
    return ['Disqualified data'] if 'LABDUC' in D else [e for b in [[k, D[k]] for k in sorted(D.keys())] for e in b]
