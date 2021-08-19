def sum_of_a_beach(s):
    return sum((s.lower().count(e) for e in ['sand', 'water', 'fish', 'sun']))
