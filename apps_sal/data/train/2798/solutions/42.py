to_alternating_case = lambda string: ''.join([[i.upper(),i.lower()][i.isupper()] for i in string])
