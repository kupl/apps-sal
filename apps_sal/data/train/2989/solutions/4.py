def bits_battle(numbers):
    evens = sum([bin(numb).replace('0b', '').count('0') for numb in numbers if numb % 2 == 0])
    odds = sum([bin(numb).replace('0b', '').count('1') for numb in numbers if numb % 2 != 0])
    return 'odds win' if odds > evens else 'evens win' if evens > odds else 'tie'
