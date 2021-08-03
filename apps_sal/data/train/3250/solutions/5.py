def short_form(s):
    return ''.join(c for i, c in enumerate(s) if c.lower() not in 'aeiou' or (i == 0 or i == len(s) - 1))
