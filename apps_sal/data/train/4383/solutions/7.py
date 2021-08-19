def is_min(i, lst):
    if i > 0:
        if i + 1 < len(lst):
            return lst[i - 1] >= lst[i] and lst[i] < lst[i + 1]
        return lst[i - 1] > lst[i]
    return lst[i] < lst[i + 1]


def is_par(i, lst):
    if i + 1 < len(lst):
        return lst[i] == lst[i + 1]
    return True


def artificial_rain(lst):
    if len(lst) in (0, 1):
        return len(lst)
    (mn, nx_mn) = (0, -1)
    i = 0
    grt = 0
    while i < len(lst):
        if is_min(i, lst):
            grt = max(grt, 1 + i - mn)
            if nx_mn == -1:
                mn = i
            else:
                mn = nx_mn
                nx_mn = -1
        else:
            nx_mn = -1
        if is_par(i, lst):
            j = i
            if i - 1 >= 0:
                j = i
                while j - 1 >= 0 and lst[j - 1] <= lst[j]:
                    j -= 1
            nx_mn = j
            while i < len(lst) and is_par(i, lst):
                i += 1
            i -= 1
        i += 1
    return max(grt, i - mn)
