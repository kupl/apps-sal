def even_numbers_before_fixed(s, f):
    return len([x for x in s[:s.index(f)] if x%2 == 0]) if f in s else -1
