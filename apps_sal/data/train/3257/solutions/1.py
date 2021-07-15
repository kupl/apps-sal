from itertools import permutations

def slogan_maker(arr):
    return list(map(' '.join, permutations(dict(list(zip(arr, list(range(len(arr)))))))))

