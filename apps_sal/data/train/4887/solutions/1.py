my_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap(year):
    return [0, 1, 0, 1, 0, 1, 1, 1][(year % 4 == 0) + (year % 100 == 0) + (year % 400 == 0) + 4 * (year < 1752)]


def day_of_year(d, m, y=2437):
    return sum(my_year[i] for i in range(1, m)) + d + is_leap(y) * (m > 2)


def days(d, m, y, d0=24, m0=3, y0=2437):
    A = day_of_year(d0, m0)
    B = sum(map(is_leap, range(y + 1, y0))) + 365 * (y0 - y)
    C = 11 * (y < 1752 or y == 1752 and day_of_year(d, m) < 246)
    D = is_leap(y) - day_of_year(d, m, y)
    return A + B - C + D
