def min_value(digits):
    new = sorted(digits)
    i = 0
    j = i + 1
    nodup = []
    stri = ''
    for i in new:
        if i not in nodup:
            nodup.append(i)
    for i in nodup:
        stri += str(i)

    return int(stri)
