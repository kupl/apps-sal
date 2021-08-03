def short_form(s):
    return s[0] + ''.join(x for x in s[1:-1] if x not in 'aeiouAEIOU') + s[-1]
