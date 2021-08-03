def solution(n):
    numeral = ''
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    print(numerals)
    def square(x, y): return int(x / number[y]) * numerals[y]
    for i in range(13):
        numeral += square(n, i)
        n = n - number[i] * int(n / number[i])
    return numeral
