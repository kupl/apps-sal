def capitalize(s, ind):
    ar = list(s)
    for (index, value) in enumerate(ar):
        for i in ind:
            if i == index:
                ar[index] = value.upper()
    return ''.join(ar)
