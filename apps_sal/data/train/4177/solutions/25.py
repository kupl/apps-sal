def men_from_boys(arr):
    odd, even = [], []
    for i in sorted(set(arr)):
        even.append(i) if i % 2 == 0 else odd.append(i)
    return even + odd[::-1]
