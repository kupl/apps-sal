def is_keith_number(n):
    i = 0
    terms = list(map(int, str(n)))
    while terms[-1] < n:
        i += 1
        terms = terms[1:] + [sum(terms)]
    return terms[-1] == n and i
