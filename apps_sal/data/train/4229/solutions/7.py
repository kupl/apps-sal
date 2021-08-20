def bits_war(numbers):
    (odd_score, even_score) = (score((x for x in numbers if x % 2)), score((x for x in numbers if x % 2 == 0)))
    return 'odds win' if odd_score > even_score else 'tie' if odd_score == even_score else 'evens win'


def score(numbers):
    return sum((bin(x)[2:].count('1') * [-1, 1][x > 0] for x in numbers))
