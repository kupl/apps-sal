def bits_battle(numbers):
    odds = 0
    evens = 0
    for n in numbers:
        if n % 2:
            odds += bin(n).count('1')
        elif n != 0 and n % 2 == 0:
            evens += bin(n)[2:].count('0')    
    return 'odds win' if odds > evens else 'evens win' if evens > odds else 'tie'
