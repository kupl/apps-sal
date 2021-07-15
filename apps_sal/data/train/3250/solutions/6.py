def short_form(s):
    n = len(s)
    return ''.join(c for i, c in enumerate(s) if c not in 'aeiouAEIOU' or (i == 0 or i == n - 1))
