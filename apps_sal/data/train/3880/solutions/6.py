def is_smooth(n):
    i = 2
    a = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            a.append(i)
    if n > 1:
        a.append(n)
    m = max(a)
    if m == 2:
        return 'power of 2'
    if m == 3:
        return '3-smooth'
    if m == 5:
        return 'Hamming number'
    if m == 7:
        return 'humble number'
    else:
        return 'non-smooth'
