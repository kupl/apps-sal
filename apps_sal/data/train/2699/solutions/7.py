base = ' thousand million billion trillion quadrillion quintillion sextillion septillion'.split(' ')
ALL = {int(i): x for i, x in zip('0 1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19 10 20 30 40 50 60 70 80 90 100'.split(), 'zero one two three four five six seven eight nine eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen ten twenty thirty forty fifty sixty seventy eighty ninety'.split(' ') + ['one hundred'])}
def parse(n): return (ALL.get(n, ALL[n // 10 * 10] + '-' + ALL[n % 10] if n < 100 else ALL[n // 100] + ' hundred ' + parse(n % 100)).strip()) if n else ''
def number2words(n): return ' '.join([parse(int(i)) + ' ' + j if int(i) else '' for i, j in zip(format(n, ',').split(',')[::-1], base)][::-1]).strip() or 'zero'  # SUPPORT UPTO SEPTILLION...
