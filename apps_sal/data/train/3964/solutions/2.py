def rank_of_element(arr, i):
    rank = 0
    for (j, value) in enumerate(arr):
        if j < i:
            if value <= arr[i]:
                rank += 1
        elif j == i:
            continue
        elif value < arr[i]:
            rank += 1
    return rank
