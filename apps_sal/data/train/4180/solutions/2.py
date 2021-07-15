def lottery(s):
    cifers = ''
    for simbol in s:
        if simbol in '1234567890' and simbol not in cifers:
            cifers = cifers + str(simbol)
    return cifers if len(cifers) else 'One more run!'
