def odd_or_even(arr):
    if(len(arr) == 0):
        return "even"
    else:
        total = 0
        for item in arr:
            total += item
        if(total % 2):
            return "odd"
        else:
            return "even"
