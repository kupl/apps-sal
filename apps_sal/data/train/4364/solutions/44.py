def odd_or_even(arr):
    sum = 0
    for i in arr:
        sum += i
    return "odd" if sum % 2 == 1 else "even"
