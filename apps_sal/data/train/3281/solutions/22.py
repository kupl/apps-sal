def unlucky_days(year):
    c = year // 100
    y = year - 100 * c
    c1 = (year - 1) // 100
    y1 = year - 1 - 100 * c1
    return (1 if (y1 + y1 // 4 + c1 // 4 - 2 * c1 + 26 * (13 + 1) // 10 + 12) % 7 == 5 else 0) + (1 if (y1 + y1 // 4 + c1 // 4 - 2 * c1 + 26 * (14 + 1) // 10 + 12) % 7 == 5 else 0) + sum(1 for m in range(3, 13) if (y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10 + 12) % 7 == 5)
