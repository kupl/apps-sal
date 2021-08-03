def find_gatecrashers(p, i): return (lambda c: [q for q in p if q not in c])({e for j, l in i for e in [j] + l})
