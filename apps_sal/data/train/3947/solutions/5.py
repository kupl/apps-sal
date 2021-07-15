def square_digits(num):
    squares = ''
    for x in str(num):
        squares += str(int(x) ** 2)
    return int(squares)
