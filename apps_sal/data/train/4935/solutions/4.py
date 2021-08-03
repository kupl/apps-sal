def infected(s):
    total = len(s) - s.count('X')
    infected = sum([len(i) for i in s.split('X') if '1' in i])
    return infected / total * 100 if total > 0 else infected
