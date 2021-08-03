def solution(n):
    ed = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    des = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    sot = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tys = ["", "M", "MM", "MMM", "MMMM"]

    return tys[n // 1000] + sot[n // 100 % 10] + des[n // 10 % 10] + ed[n % 10]
