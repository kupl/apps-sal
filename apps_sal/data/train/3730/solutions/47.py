def capitalize(s):
    case_1 = ''
    case_2 = ''
    for i in range(len(s)):
        if i % 2 == 0:
            case_1 += s[i].upper()
        else:
            case_1 += s[i].lower()
    for i in range(len(s)):
        if i % 2 == 0:
            case_2 += s[i].lower()
        else:
            case_2 += s[i].upper()
    return [case_1, case_2]
