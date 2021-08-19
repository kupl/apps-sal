def men_from_boys(arr):
    (men, boys) = ([], [])
    for n in sorted(set(arr)):
        boys.append(n) if n % 2 else men.append(n)
    return men + boys[::-1]
