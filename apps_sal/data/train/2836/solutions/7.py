def find_screen_height(width, ratio):
    (wr, rr) = (int(n) for n in ratio.split(':'))
    return f'{width}x{width * rr // wr}'
