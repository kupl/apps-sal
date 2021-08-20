def something_acci(num_digits):
    (a, b, c, d, e, f) = (1, 1, 2, 2, 3, 3)
    count = 6
    while True:
        sf = str(f)
        if len(sf) >= num_digits:
            return (count, len(sf))
        (a, b, c, d, e, f) = (b, c, d, e, f, d * e * f - a * b * c)
        count += 1
