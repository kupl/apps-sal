def first_non_repeating_letter(s):
    for c in s:
        if s.count(c) + s.count(c.swapcase()) * c.isalpha() == 1:
            return c
    return ''
