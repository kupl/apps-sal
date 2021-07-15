powerset=lambda n: (lambda c: c+[[n[0]]+e for e in c])(powerset(n[1:])) if n else [[]]
