def odd_or_even(arr):
    res = sum(map(int,arr))
    return "even" if res % 2 == 0 else "odd"

s = [0, 1, 3]
print(odd_or_even(s))
