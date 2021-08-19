UNITS = ' one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ')
TENS = ' ten twenty thirty forty fifty sixty seventy eighty ninety'.split(' ')
UNITS += [TENS[n // 10] + '-' + UNITS[n % 10] if n % 10 else TENS[n // 10] for n in range(20, 100)]


def number2words(n):
    if n == 0:
        return 'zero'
    text = []
    if n >= 1000:
        text.append(number2words(n // 1000) + ' thousand')
        n %= 1000
    (hundred, unit) = divmod(n, 100)
    if hundred:
        text.append(UNITS[hundred] + ' hundred')
    if unit:
        text.append(UNITS[unit])
    return ' '.join(text)
