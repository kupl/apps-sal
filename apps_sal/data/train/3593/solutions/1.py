def capitalize(s, ind):
    result = list(s)
    for index in ind:
        try:
            result[index] = result[index].upper()
        except IndexError:
            break  # assumes the indexes are sorted
    return ''.join(result)

