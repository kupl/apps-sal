def to_alternating_case(string): return ''.join([[i.upper(), i.lower()][i.isupper()] for i in string])
