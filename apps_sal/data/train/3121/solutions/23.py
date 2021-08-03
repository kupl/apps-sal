def solve(arr):
    positive = sorted([x for x in arr if x >= 0])
    negative = sorted([x for x in arr if x < 0], reverse=True)
    longer_index = len(positive) <= len(negative)
    longer = [positive, negative][longer_index]
    for i in [positive, negative][not longer_index]:
        longer.remove(-i)
    return longer[0]
