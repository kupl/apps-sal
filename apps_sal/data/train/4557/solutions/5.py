def row_weights(lst):
    return (sum(lst[i] for i in range(0, len(lst), 2)),) + (sum(lst[j] for j in range(1, len(lst), 2)),)
