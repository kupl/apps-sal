def roman_fractions(integer, fraction=0):
    if not 0 <= integer <= 5000 or not 0 <= fraction < 12:
        return "NaR"
    if not integer and not fraction: return "N"
    m, n = divmod(integer, 1000)
    roman = "M" * m
    c, n = divmod(n, 100)
    roman += ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"][c]
    x, i = divmod(n, 10)
    roman += ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"][x]
    roman += ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"][i]
    roman += ["", ".", ":", ":.", "::", ":.:", "S", "S.", "S:", "S:.", "S::", "S:.:"][fraction]
    return roman
