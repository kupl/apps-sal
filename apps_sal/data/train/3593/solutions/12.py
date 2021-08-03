def capitalize(s, ind):
    list_s = list(s)
    cap = []

    for i in range(len(list_s)):
        if i in ind:
            list_s[i] = list_s[i].upper()
        cap.append(list_s[i])

    cap_s = ''.join(cap)
    return cap_s
