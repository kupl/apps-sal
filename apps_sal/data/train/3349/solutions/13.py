def find_missing_number(w):
    return (lambda s: min(set(range(max(s))) - s or [0]))((set(w) <= set('0123456789 ') and set(map(int, w.split())) or {2}) | {w == ''})
