def areYouPlayingBanjo(name):
    name_lower = name.lower()
    letters_lst = []
    for item in name_lower:
        letters_lst.append(item)
    if letters_lst[0] == 'r':
        result = name + ' plays banjo'
    else:
        result = name + ' does not play banjo'
    return result
