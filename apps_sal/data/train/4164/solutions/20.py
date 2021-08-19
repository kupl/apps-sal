def first_non_repeating_letter(str1):
    str2 = str1.lower()
    for c in str2:
        if str2.count(c) == 1:
            return str1[str2.index(c)]
    return ''
