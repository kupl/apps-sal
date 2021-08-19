def even_digit_squares(a, b):
    return [i ** 2 for i in range(int(a ** 0.5), int(b ** 0.5) + 1) if all((not int(j) % 2 for j in str(i ** 2)))]
