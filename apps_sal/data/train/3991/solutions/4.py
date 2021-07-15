def highest_rank(arr):
    frequent = {}
    for i in arr:
        if i not in frequent:
            frequent[i] = 0
        frequent[i] += 1
    ordered_inv = sorted(list(frequent.items()), key=lambda x: (x[1],x[0]), reverse=True)
    return ordered_inv[0][0]

