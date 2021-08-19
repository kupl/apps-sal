def word_mesh(arr):
    overlaps = [max(filter(prev.endswith, (word[:k] for k in range(len(word) + 1)))) for (prev, word) in zip(arr, arr[1:])]
    return ''.join(overlaps) if all(overlaps) else 'failed to mesh'
