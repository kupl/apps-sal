def odd_or_even(arr):
    return {1:'odd', 0:'even'}[sum(arr) % 2]
