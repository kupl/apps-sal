def find_min_max_product(arr, k):

    if k > len(arr):
        return None

    if k == 1:
        return min(arr), max(arr)

    if k == len(arr):
        res = eval('*'.join([str(i) for i in arr]))
        return res, res

    arr = sorted(arr)

    arr_abs = sorted([abs(i) for i in arr])
    max_abs = max(arr_abs)
    pos = len([i for i in arr if i > 0])
    pos_all = [i for i in arr if i > 0]
    neg_all = [i for i in arr if i < 0]
    neg = len([i for i in arr if i < 0])
    zer = len([i for i in arr if i == 0])

    if pos == 0 and zer == 0 and k % 2 == 0:
        min_both = arr[-k:]
        max_both = arr[:k]

    if pos == 0 and zer == 0 and k % 2 != 0:
        min_both = arr[:k]
        max_both = arr[-k:]

    if pos == 0 and zer != 0 and k % 2 == 0:
        min_both = [0]
        max_both = arr[:k]

    if pos == 0 and zer != 0 and k % 2 != 0:
        min_both = arr[:k]
        max_both = [0]

    if neg == 0 and zer == 0:
        min_both = arr[:k]
        max_both = arr[-k:]

    if neg == 0 and zer != 0:
        min_both = [0]
        max_both = arr[-k:]

    if pos != 0 and neg != 0:
        for_sort = sorted([[i, abs(i)] for i in arr], key=lambda i: i[1])
        for_sort = [i[0] for i in for_sort]

        all_pos = [i for i in for_sort if i > 0]
        all_neg = [i for i in for_sort if i < 0]

        max_pos = [i for i in for_sort[-k:] if i > 0]
        max_neg = [i for i in for_sort[-k:] if i < 0]

        for i in range(len(all_pos) - len(max_pos)):
            max_pos.insert(0, 0)

        for i in range(len(all_neg) - len(max_neg)):
            max_neg.insert(0, 0)

        pos_reserve = [a - b for a, b in zip(all_pos, max_pos)]
        neg_pos_reserve = [a - b for a, b in zip(all_neg, max_neg)]

        pos_reserve = [i for i in pos_reserve if not i == 0]
        neg_pos_reserve = sorted([i for i in neg_pos_reserve if not i == 0])
        max_pos = [i for i in max_pos if not i == 0]
        max_neg = [i for i in max_neg if not i == 0]

        max_pos_alt = [i for i in for_sort[-k:] if i > 0]
        max_neg_alt = [i for i in for_sort[-k:] if i < 0]

        if len(max_neg) > 0 and len(max_neg) % 2 and len(pos_reserve) > 0:
            max_neg.pop(0)
            max_pos.append(pos_reserve[-1])
            if len(max_pos_alt) > 0 and len(neg_pos_reserve) > 0:
                max_pos_alt.pop(0)
                max_neg_alt.append(neg_pos_reserve[0])
        elif len(max_neg) > 0 and len(max_neg) % 2 and len(pos_reserve) == 0:
            max_pos.pop(0)
            max_neg.append(neg_pos_reserve[0])
        elif len(max_neg) == 1 and len(neg_pos_reserve) > 0:
            max_pos.pop(0)
            max_neg.append(neg_pos_reserve[0])
        elif len(max_neg) == 1 and len(pos_reserve) > 0:
            max_neg.pop(0)
            max_pos.append(pos_reserve[0])

        min_pos = [i for i in for_sort[-k:] if i > 0]
        min_neg = [i for i in for_sort[-k:] if i < 0]

        for i in range(len(all_pos) - len(min_pos)):
            min_pos.insert(0, 0)

        for i in range(len(all_neg) - len(min_neg)):
            min_neg.insert(0, 0)

        neg_reserve = [a - b for a, b in zip(all_neg, min_neg)]
        pos_reserve_neg = [a - b for a, b in zip(all_pos, min_pos)]

        neg_reserve = sorted([i for i in neg_reserve if not i == 0])
        pos_reserve_neg = [i for i in pos_reserve_neg if not i == 0]

        pos_reserve_neg_alt = pos_reserve_neg

        min_pos = [i for i in min_pos if not i == 0]
        min_neg = [i for i in min_neg if not i == 0]

        min_pos_alt = [i for i in for_sort[-k:] if i > 0]
        min_neg_alt = [i for i in for_sort[-k:] if i < 0]

        if not len(min_neg) % 2:
            if len(min_neg_alt) > 0 and len(pos_reserve_neg_alt) > 0:
                min_neg_alt.pop(0)
                min_pos_alt.append(pos_reserve_neg_alt[-1])
            try:
                min_neg.append(neg_reserve[0])
                min_pos.pop(0)
            except:
                try:
                    min_neg.pop(0)
                    min_pos.append(pos_reserve_neg[-1])
                except:
                    pass

        elif not len(min_neg) % 2 and 0 in arr:
            min_neg.append(0)

        max_both = max_pos + max_neg
        max_both_alt = max_pos_alt + max_neg_alt

        min_both = min_pos + min_neg
        min_both_alt = min_pos_alt + min_neg_alt

    mn = eval('*'.join([str(i) for i in min_both]))
    mx = eval('*'.join([str(i) for i in max_both]))

    try:
        mx_alt = eval('*'.join([str(i) for i in max_both_alt]))
    except:
        mx_alt = -10**1000

    try:
        mn_alt = eval('*'.join([str(i) for i in min_both_alt]))
    except:
        mn_alt = 10**1000

    return min(mn, mn_alt), max(mx, mx_alt)
