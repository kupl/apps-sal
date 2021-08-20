def decToHex(n):
    hexChart = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexValue = ''
    while n:
        hexValue = hexChart[n % 16] + hexValue
        n //= 16
    return hexValue


def hexToDec(string):
    hex = '0123456789ABCDEF'
    total = 0
    for (index, i) in enumerate(string):
        value = hex.index(i)
        power = len(string) - (index + 1)
        total += value * 16 ** power
    return total


def coffee_limits(year, month, day):
    cafe = hexToDec('CAFE')
    cafeCups = 0
    h = int(str(year) + str(month).zfill(2) + str(day).zfill(2))
    for i in range(5000):
        h += cafe
        cafeCups += 1
        if 'DEAD' in decToHex(h):
            break
    h = int(str(year) + str(month).zfill(2) + str(day).zfill(2))
    print(h)
    decaf = hexToDec('DECAF')
    decafCups = 0
    for i in range(5000):
        h += decaf
        decafCups += 1
        if 'DEAD' in decToHex(h):
            break
    return [cafeCups % 5000, decafCups % 5000]
