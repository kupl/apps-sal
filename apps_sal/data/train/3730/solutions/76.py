def capitalize(s):
    even = ''
    odd = ''
    for i, c in enumerate(s):
        if i % 2 == 0:
            even += c.upper()
            odd += c
        else:
            even += c
            odd += c.upper()

    return [even, odd]
