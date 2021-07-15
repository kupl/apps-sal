def infected_zeroes(a):
    s = ''.join(str(e) for e in a)
    return max([len(w) + 1 for w in s.split('0')] + [s.find('0') * 2, s[::-1].find('0') * 2]) // 2
