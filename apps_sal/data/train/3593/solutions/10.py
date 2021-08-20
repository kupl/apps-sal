def capitalize(s, ind):
    result = ''
    for (index, letter) in enumerate(s):
        if index in ind:
            result += letter.upper()
        else:
            result += letter
    return result
