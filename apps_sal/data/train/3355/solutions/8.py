def solve(n):
    min_cost = -1
    s = str(n)[::-1]
    for pair in ('00', '25', '50', '75'):
        cost = calculate_ending_pair_cost(s, pair)
        if min_cost == -1 or (cost != -1 and cost < min_cost):
            min_cost = cost
    return min_cost


def calculate_ending_pair_cost(s, pair):
    indices = find_lowest_places(s, pair)
    if indices is None:
        return -1
    cost = 1 if indices[1] > indices[0] else 0
    if cost == 1:
        indices = (indices[1], indices[0])
    cost += indices[0] - indices[1] - 1
    cost += 2 * indices[1]
    if len(s) > 2:
        non_zero_index = first_non_zero_digit_after_indices(s, indices)
        if non_zero_index is None:
            return -1
        cost += len(s) - 1 - non_zero_index
        cost -= 1 if indices[0] > non_zero_index else 0
        cost -= 1 if indices[1] > non_zero_index else 0
    return cost


def find_lowest_places(s, pair):
    (d10, d1) = pair
    try:
        i1 = s.index(d1)
    except:
        return None
    start = 0
    if d1 == d10:
        start = i1 + 1
    try:
        i10 = s.index(d10, start)
    except:
        return None
    return (i10, i1)


def first_non_zero_digit_after_indices(s, indices):
    s = s[::-1]
    indices = [len(s) - 1 - indices[i] for i in range(len(indices))]
    non_zero_index = None
    for i in range(len(s)):
        if i not in indices and s[i] != '0':
            non_zero_index = i
            break
    if non_zero_index is None:
        return None
    return len(s) - 1 - non_zero_index
