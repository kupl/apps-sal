def bits_war(numbers):
    evens = sum([bin(numb).replace('0b', '').count('1') * (-1 if '-' in bin(numb) else 1) for numb in numbers if numb % 2 == 0])
    odds = sum([bin(numb).replace('0b', '').count('1') * (-1 if '-' in bin(numb) else 1) for numb in numbers if numb % 2 != 0])
    return 'odds win' if odds > evens else 'evens win' if evens > odds else 'tie'
