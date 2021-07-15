def capitalize(s,ind):
    arr = []
    for i, el in enumerate(s):
        if i in ind:
            arr.append(el.upper())
        else:
            arr.append(el)
    return "".join(arr)
