def array_leaders(n):
    return [n[i] for i in range(len(n)) if sum(n[i+1:]) < n[i]]
