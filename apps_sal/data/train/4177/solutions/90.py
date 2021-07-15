def men_from_boys(arr):
    return sorted(i for i in set(arr) if i%2==0) + sorted([i for i in set(arr) if i%2!=0], reverse = True)

