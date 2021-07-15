def array_leaders(N):
    return [n for i, n in enumerate(N) if n>sum(N[i+1:])]
