def is_smooth(n, p=0):
    return ['power of 2', '3-smooth', 'Hamming number', 'humble number', 'non-smooth'][p] if n < 2 or p > 3 else is_smooth(n, p + 1) if n % [2, 3, 5, 7, 11][p] else is_smooth(n // [2, 3, 5, 7, 11][p], p)
