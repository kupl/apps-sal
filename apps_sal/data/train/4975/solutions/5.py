def solution(n):
    dic = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman = ''
    for a in reversed(sorted(dic.keys())):
        while a <= n:
            n = n - a
            roman = roman + dic[a]
    return roman
