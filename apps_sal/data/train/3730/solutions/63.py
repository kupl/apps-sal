def capitalize(s):
    (odd, even) = ([], [])
    for (i, a) in enumerate(s):
        if i % 2 == 0:
            even.append(a.capitalize())
            odd.append(a)
        else:
            even.append(a)
            odd.append(a.capitalize())
    return [''.join(even)] + [''.join(odd)]
