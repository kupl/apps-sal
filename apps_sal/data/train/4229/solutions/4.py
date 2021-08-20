def bits_war(numbers):
    (even, odd) = (0, 0)
    for x in numbers:
        res = bin(x).count('1')
        res = -res if x < 0 else res
        if x % 2:
            odd += res
        else:
            even += res
    return 'tie' if even == odd else ('even', 'odd')[odd > even] + 's win'
