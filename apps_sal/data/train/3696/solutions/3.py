def add(l):
    return [sum(l[:i+1]) for i in range(0,len(l))] if all(isinstance(x, int) for x in l) and isinstance(l, list) else 'Invalid input'
