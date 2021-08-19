def nQueen(n):
    if 2 <= n <= 3:
        return []
    sol = list(range(n))
    (even, odd) = (sol[::2], sol[1::2])
    if n % 6 == 2:
        even = even[1::-1] + even[3:] + even[2:3]
    if n % 6 == 3:
        (even, odd) = (even[2:] + even[:2], odd[1:] + odd[:1])
    return odd + even
