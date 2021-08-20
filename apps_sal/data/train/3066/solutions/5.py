def solve(p):
    return '{}{}'.format('$', ''.join([['+', '-'][(len([j for j in range(len(p[:i])) if p[j:j + 2] == '-(' and (not len([k for k in range(len(p[:i])) if k > j and p[k] == ')' and (p[j:k].count(')') < p[j:k].count('('))]))]) + int(p[i - 1] == '-')) % 2] + c for (i, c) in enumerate(p) if c not in ['(', ')', '+', '-']])).replace('$+', '').replace('$', '')
