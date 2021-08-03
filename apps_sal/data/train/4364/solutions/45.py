def odd_or_even(arr):

    if arr == []:
        arr = [0]

    total = sum(arr)

    if total % 2 == 0 or total == 0:
        return "even"
    else:
        return "odd"
