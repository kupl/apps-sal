from itertools import combinations


def find_zero_sum_groups(my_list, n):
    my_list = list(set(my_list))
    if len(my_list) == 0:
        return 'No elements to combine'
    subs = []
    sumsubs = []
    for i in range(n, n + 1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp) > 0:
            subs.extend(temp)
    subs.sort()
    for x in subs:
        x.sort()
        if sum(x) == 0 and x not in sumsubs:
            sumsubs.append(x)
    for x in sumsubs:
        x.sort()
    sumsubs.sort(key=lambda x: x[0])
    sumsubs.sort()
    if len(sumsubs) == 1:
        return sumsubs[0]
    if len(sumsubs) > 1:
        return sumsubs
    else:
        return 'No combinations'
