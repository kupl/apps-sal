numerals = {
        "-":"负",
        ".":"点",
        0:"零",
        1:"一",
        2:"二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
        10:"十",
        100:"百",
        1000:"千",
        10000:"万"
    }

def to_chinese_numeral(n, keep_ten=False, trailing_zero=False):
    if trailing_zero: return numerals[0] + to_chinese_numeral(n, keep_ten)
    if n < 0: return numerals['-'] + to_chinese_numeral(-n)
    if n % 1: return to_chinese_numeral(n // 1) + numerals['.'] + ''.join(numerals[int(d)] for d in str(n).split('.')[1])
    if n >= 10000: return to_chinese_numeral(n // 10000) + numerals[10000] + bool(n % 10000) * to_chinese_numeral(n % 10000, True, n % 10000 < 10000 // 10)
    if n >= 1000: return numerals[n // 1000] + numerals[1000] + bool(n % 1000) * to_chinese_numeral(n % 1000, True, n % 1000 < 1000 // 10)
    if n >= 100: return numerals[n // 100] + numerals[100] + bool(n % 100) * to_chinese_numeral(n % 100, True, n % 100 < 100 // 10)
    if n >= 10: return bool(keep_ten or n // 10 > 1) * numerals[n // 10] + numerals[10] + bool(n % 10) * to_chinese_numeral(n % 10, True)
    return numerals[n]
