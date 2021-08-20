def first_non_repeating_letter(string):
    cass = ''.join(string)
    chars = list((i.lower().replace(' ', '') for i in cass))
    newList = []
    for (char, i) in zip(chars, string):
        count = chars.count(char)
        if count >= 2:
            continue
        else:
            newList.append(i)
    if len(newList) > 0:
        return str(newList[0])
    else:
        return ''
