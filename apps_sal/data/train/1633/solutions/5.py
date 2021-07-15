def to_chinese_numeral(n):
    numerals = {"-":"负", ".":"点", 0:"零", 1:"一", 2:"二", 3:"三", 4:"四", 5:"五", 6:"六", 7:"七", 8:"八", 9:"九", 10:"十", 100:"百", 1000:"千", 10000:"万"}
    start, end = '', ''
    if str(n).count('.') == 1:
        end, s = numerals['.'], str(n)
        for i in range(s.index('.') + 1, len(s)):
            end += numerals[int(s[i])]
        n = int(s[:s.index('.')])
    if n < 0:
        start += numerals['-']
        n *= -1
    if n < 11:
        start += numerals[n]
        return start + end
    elif n < 20:
        return start + numerals[10] + numerals[n % 10]
    tth, n = n // 10000, n - n // 10000 * 10000
    th, n = n // 1000, n - n // 1000 * 1000
    h, n = n // 100, n - n // 100 * 100
    t, n = n // 10, n - n // 10 * 10
    if tth > 0 and th == h == t == n == 0:
        start += numerals[tth] + numerals[10000]
    else:
        if tth > 0:
            start += numerals[tth] + numerals[10000]
        if th > 0 and h == t == n == 0:
            start += numerals[th] + numerals[1000]
        else:
            if th > 0:
                start += numerals[th] + numerals[1000]
            elif tth > 0 and th == 0:
                start += numerals[0]
            if h > 0 and t == n == 0:
                start += numerals[h] + numerals[100]
            else:
                if h > 0:
                    start += numerals[h] + numerals[100]
                elif th > 0 and h == 0:
                    start += numerals[0]
                if t > 0:
                    start += numerals[t] + numerals[10]
                elif h > 0 and t == 0:
                    start += numerals[0]
                if n > 0:
                    start += numerals[n]
    
    return start + end

