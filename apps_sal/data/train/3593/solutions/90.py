def capitalize(s, ind):
    arr = []
    for i, letter in enumerate(s):
        if i in ind:
            arr.append(letter.upper())
        else:
            arr.append(letter)
    return "".join(arr)
