def trotter(k):
    if not k:
        return "INSOMNIA"
    d = set()
    for n in range(k, k*73, k):
        d.update(set(str(n)))
        if len(d) == 10:
            return n
