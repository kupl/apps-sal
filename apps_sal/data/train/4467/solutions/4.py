def remember(s):
    li, final = [], []
    for i in s:
        if i not in li:
            li.append(i)
        else:
            final.append(i)
    return sorted(set(final), key=final.index)
