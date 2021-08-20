def odd_or_even(arr):
    return 'even' if sum([n % 2 != 0 for n in arr]) % 2 == 0 else 'odd'
