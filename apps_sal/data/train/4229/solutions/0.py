def bits_war(numbers):
    odd, even = 0, 0
    for number in numbers:
        if number % 2 == 0:
            if number > 0:
                even += bin(number).count('1')
            else:
                even -= bin(number).count('1')
        else:
            if number > 0:
                odd += bin(number).count('1')
            else:
                odd -= bin(number).count('1')
    return 'odds win' if odd > even else 'evens win' if even > odd else 'tie'
