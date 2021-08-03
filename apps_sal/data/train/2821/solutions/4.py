def trim(beard):
    for i, a in enumerate(beard):
        if i != len(beard) - 1:
            beard[i] = ['|' if v in 'J|' else v for v in a]
        else:
            beard[i] = ['...' for v in a]
    return beard
