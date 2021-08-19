def remove_exclamation_marks(s):
    total = ''
    for i in s:
        if i != '!':
            total += i
    return total
