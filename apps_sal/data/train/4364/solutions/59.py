def odd_or_even(arr):
    n = sum(arr)
    odd = [1,3,5,7,9]
    even = [2,4,6,8,0]
    if (n % 10) in odd:
        return "odd"
    else:
        return "even"
