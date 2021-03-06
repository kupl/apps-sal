def roman_fractions(integer, fraction=0):
    fracs = ['.', ':', ':.', '::', ':.:', 'S', 'S.', 'S:', 'S:.', 'S::', 'S:.:']
    res = 'NaR'
    if integer >= 0 and integer <= 5000 and (fraction >= 0) and (fraction <= 11):
        print(integer, fraction)
        res = ''
        if integer == 0 and fraction == 0:
            return 'N'
        while integer > 0:
            if integer >= 1000:
                res += 'M'
                integer -= 1000
            elif integer >= 900:
                res += 'CM'
                integer -= 900
            elif integer >= 500:
                res += 'D'
                integer -= 500
            elif integer >= 400:
                res += 'CD'
                integer -= 400
            elif integer >= 100:
                res += 'C'
                integer -= 100
            elif integer >= 90:
                res += 'XC'
                integer -= 90
            elif integer >= 50:
                res += 'L'
                integer -= 50
            elif integer >= 40:
                res += 'XL'
                integer -= 40
            elif integer >= 10:
                res += 'X'
                integer -= 10
            elif integer >= 9:
                res += 'IX'
                integer -= 9
            elif integer >= 5:
                res += 'V'
                integer -= 5
            elif integer >= 4:
                res += 'IV'
                integer -= 4
            elif integer >= 1:
                res += 'I'
                integer -= 1
        "\n        while(fraction>0):\n            if(fraction>=6):\n                res+='S'\n                fraction-=6\n            elif(fraction>=2):\n                res+=':'\n                fraction-=2\n            elif(fraction>=1):\n                res+='.'\n                fraction-=1\n        "
        if fraction > 0:
            res += fracs[fraction - 1]
    return res
