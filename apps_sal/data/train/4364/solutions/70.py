def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(odd_or_even(s))
