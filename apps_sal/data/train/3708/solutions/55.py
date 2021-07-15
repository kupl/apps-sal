def hex_to_dec(s):
    dict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    s = s[::-1]
    liczba = 0
    for i in range(len(s)):
        liczba += dict[s[i]]*(16**i)
    return liczba
