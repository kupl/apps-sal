def find(a):
    return (max(a) + min(a)) * (len(a) + 1) / 2 - sum(a)
