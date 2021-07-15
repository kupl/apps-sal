from collections import Counter

def highest_rank(arr):
    return max(Counter(arr).items(), key=lambda x: [x[1], x[0]])[0]
