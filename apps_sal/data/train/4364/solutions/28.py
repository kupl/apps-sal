def odd_or_even(arr):
    sum=0
    for char in arr:
        sum = sum + int(char)
    return "even" if sum % 2 == 0 else "odd"

