def men_from_boys(arr):
    return sorted(list(set([i for i in arr if i % 2 == 0]))) + sorted(list(set([i for i in arr if i % 2 != 0])))[::-1]
