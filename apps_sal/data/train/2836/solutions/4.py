def find_screen_height(width, ratio):
    (a, b) = map(int, ratio.split(':'))
    return f'{width}x{width * b // a}'
