def odd_or_even(arr):
    t = 0
    for i in arr:
        t += i
    return "even" if t%2==0 else "odd"
