def first_non_repeating_letter(string):
    try:
        return next(c for c in string if string.lower().count(c.lower()) == 1)
    except StopIteration:
        return ''
