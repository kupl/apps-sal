def learn_charitable_game(arr):
    if min(arr) <= 0 and max(arr) <= 0:
        return False
    tot = sum(arr)
    mean = round(tot / len(arr))
    result = sum((mean - x for x in arr))
    return result == 0
