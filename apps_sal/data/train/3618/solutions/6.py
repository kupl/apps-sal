def socialist_distribution(p, m):
    return [] if sum(p) < m * len(p) else p if all((m <= e for e in p)) else (lambda mini, maxi: socialist_distribution(p[:mini] + [p[mini] + 1] + p[mini + 1:maxi] + [p[maxi] - 1] + p[maxi + 1:], m) if mini < maxi else socialist_distribution(p[:maxi] + [p[maxi] - 1] + p[maxi + 1:mini] + [p[mini] + 1] + p[mini + 1:], m))(p.index(min(p)), p.index(max(p)))
