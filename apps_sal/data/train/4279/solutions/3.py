def group_in_10s(*li):
    (li, result, ini, i) = (sorted(li), [], 10, 0)
    while i < len(li):
        temp = []
        while i < len(li) and li[i] < ini:
            temp.append(li[i])
            i += 1
        result.append(temp or None)
        ini += 10
    return result
