def str_count(strng, letter):
    Liste = list(strng)
    Counts = dict()
    for ch in Liste:
        if ch not in Counts:
            Counts[ch] = 1
        else:
            Counts[ch] = Counts[ch] + 1
    if letter in Counts:
        return Counts[letter]
    else:
        return 0
    return Counts[letter]
