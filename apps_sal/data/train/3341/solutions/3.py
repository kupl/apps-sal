def pop_shift(string):
    mid = len(string) // 2
    return [string[::-1][:mid], string[:mid], string[mid : len(string)-mid]]
