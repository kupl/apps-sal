def past(h, m, s):
    if 0 <= h <= 23 or 0 <= m <= 59 or 0 <= s <= 59:
        x = h * 3600000
        y = m * 60000
        z = s * 1000
        total = x + y + z
        return total
    else:
        return 'Please input an hour between 0 and 23 and a minute or second inbetween 0 and 59.'
