def spin_solve(s):
    return ' '.join([[[[i, '0'][len(i) == 1], i.upper()][len(i) - (i[-1].isalpha() ^ 1) == 2 or i[-1] == ','], i[:len(i) if i[-1].isalpha() else -1][::-1] + [i[-1], ''][i[-1].isalpha()]][len(i) - (i[-1].isalpha() ^ 1) > 6 or i.lower().count('t') > 1] for i in s.split()])
