from string import ascii_letters

sortable = frozenset(ascii_letters)

def sort_string(s):
    sorted_chars = iter(sorted((c for c in s if c in sortable), key=str.lower))
    return ''.join(next(sorted_chars) if c in sortable else c for c in s)
