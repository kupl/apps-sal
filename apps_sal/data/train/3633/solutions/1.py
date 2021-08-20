def shuffle_it(arr, *ind):
    for (a, b) in ind:
        [arr[b], arr[a]] = [arr[a], arr[b]]
    return arr
