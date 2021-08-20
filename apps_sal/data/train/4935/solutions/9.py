def infected(s):
    if '1' not in s:
        return 0
    s = s.split('X')
    return sum((len(i) for i in s if '1' in i)) / sum(map(len, s)) * 100
