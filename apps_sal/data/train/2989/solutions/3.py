def bits_battle(numbers):
    odds = [i for i in numbers if i % 2]
    evens = [i for i in numbers if i % 2 == 0]
    res = sum((bin(i).count('1') for i in odds)) - sum((bin(i)[2:].count('0') for i in evens))
    return 'tie' if res == 0 else ['odds win', 'evens win'][res < 0]
