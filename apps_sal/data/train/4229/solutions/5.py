def bits_war(numbers):
    scores = sum((f'{n:b}'.count('1') * (-1) ** (n % 2 == (n > 0)) for n in numbers))
    return f"{['odds', 'evens'][scores > 0]} win" if scores else 'tie'
