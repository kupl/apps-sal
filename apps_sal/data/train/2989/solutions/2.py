def bits_battle(numbers):
    x = sum(format(n, 'b').count('1') if n % 2 else -format(n, 'b').count('0') for n in numbers if n)
    return (
        'odds win' if x > 0 else
        'evens win' if x < 0 else
        'tie'
    )
