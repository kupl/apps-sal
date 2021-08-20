def weight_words(nam):
    sum = 0
    for x in nam:
        sum += ord(x) - 96
    return sum + len(nam)


def rank(st, we, n):
    index = 0
    if len(st) == 0:
        return 'No participants'
    lst_st = st.split(',')
    if n > len(lst_st):
        return 'Not enough participants'
    res = []
    for (name, w) in zip(lst_st, we):
        res.append((weight_words(name.lower()) * w, name))
    res = sorted(res, reverse=True)
    while index < len(res) - 1:
        tmp = res[index]
        tmp_next = res[index + 1]
        if tmp[0] == tmp_next[0]:
            if tmp[1] > tmp_next[1]:
                (res[index], res[index + 1]) = (res[index + 1], res[index])
            else:
                index = index + 1
        else:
            index = index + 1
    return res[n - 1][1]
