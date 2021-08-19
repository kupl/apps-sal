def bears(x, s):
    couples = ['B8', '8B']
    matches = ['', False]
    counter = 0
    ln = len(s)
    i = 0
    while i < ln:
        pair = s[i:i + 2]
        if pair in couples:
            matches[0] += pair
            counter += 1
            i += 2
        else:
            i += 1
    if counter >= x:
        matches[1] = True
    return matches
