import itertools


def choose_best_sum(t, k, ls):
    print(t, k, ls)
    list_sorted = sorted(ls)
    x = sum(list_sorted[:k])
    if x > t:
        return None
    else:
        new_list = []
        for i in range(0, len(ls) + 1):
            for subset in itertools.combinations(ls, k):
                if sum(subset) <= t:
                    new_list.append(sum(subset))
        if len(new_list) == 0:
            return None
        else:
            return max(new_list)
