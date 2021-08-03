def first_non_repeating_letter(n):
    for i in n:
        if n.lower().count(i.lower()) == 1:
            return i
    return ''
