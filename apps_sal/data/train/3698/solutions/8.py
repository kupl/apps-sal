def tiy_fizz_buzz(string):
    def r(i): return {i in 'euioa': "Yard",
                      i in 'EUIOA': "Iron Yard",
                      i in 'QWRTYPSDFGHJKLZXCVBNM': 'Iron',
                      not i in 'euioaEUIOAQWRTYPSDFGHJKLZXCVBNM': i}[True]
    return ''.join([r(i) for i in string])
