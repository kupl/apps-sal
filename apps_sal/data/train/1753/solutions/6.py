def least_bribes(bribes):
    d = dict()
    result = dp_worst_case(d, 0, len(bribes) - 1, bribes)
    return result


def dp_worst_case(d, start, end, l):
    if start in d:
        if end in d[start]:
            return d[start][end]
    diff = end - start
    if diff == 0:
        return l[start]
    elif diff == 1:
        return l[start] + l[end]
    elif diff == 2:
        return max([l[start + 1] + l[start], l[start + 1] + l[end]])
    else:
        anchor_wc_list = list()
        for i in range(diff + 1):
            if i == 0 or i == diff:
                continue
            else:
                anchor = start + i
                wcleft = l[anchor] + dp_worst_case(d, start, anchor - 1, l)
                wcright = l[anchor] + dp_worst_case(d, anchor + 1, end, l)
                anchor_wc_list.append(max([wcleft, wcright]))
        result = min(anchor_wc_list)
        if start in d:
            d[start][end] = result
        else:
            d[start] = dict()
            d[start][end] = result
        return result
