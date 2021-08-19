best_sums = {}


def choose_best_sum(t, k, ls):
    ls = [x for x in ls if x <= t]
    if k > len(ls):
        return None
    if k == 1:
        best_sum = max(ls)
        return best_sum
    ls.sort()
    the_tuple = tuple([t] + [k] + ls)
    best_sum = best_sums.get(the_tuple)
    if best_sum is not None:
        return best_sum
    else:
        i = 0
        best_sum = None
        while i < len(ls):
            nt = t - ls[i]
            s = choose_best_sum(nt, k - 1, ls[0:i] + ls[i + 1:])
            if s is None:
                del ls[i]
                continue
            else:
                best_sum = max(0 if best_sum is None else best_sum, s + ls[i])
                if best_sum == t:
                    best_sums[the_tuple] = best_sum
                    return best_sum
            i += 1
    if best_sum is not None:
        best_sums[the_tuple] = best_sum
    return best_sum
