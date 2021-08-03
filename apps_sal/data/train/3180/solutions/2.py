def trotter(n):
    if n == 0:
        return "INSOMNIA"
    seen, current = set(str(n)), n
    while len(seen) < 10:
        current += n
        seen.update(str(current))
    return current
