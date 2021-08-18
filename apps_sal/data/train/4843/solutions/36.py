import itertools


def choose_best_sum(t, k, ls):
    combinations = list(itertools.combinations(ls, k))
    sum_list = []
    min_ostatok = t
    result = None
    for item in combinations:
        sum_list.append(sum(item))
    for summa in sum_list:
        if summa <= t:
            if min_ostatok > (t - summa) and (summa - t) <= 0:
                result = summa
                min_ostatok = t - summa
                print(min_ostatok)
    print(result)
    return result
