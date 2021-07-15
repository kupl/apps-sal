def bits_war(numbers):
    even, odd = (
        sum(bin(x).count('1') * (1 if x > 0 else -1)
        for x in numbers if x % 2 == remainder) for remainder in [0, 1]
    )
    return (
        'odds win' if odd > even else
        'evens win' if even > odd else
        'tie'
    )
