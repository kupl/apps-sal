special = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}


def three_digits2words(s):
    """ len of s should <= 3 """
    s = str(int(s))
    if s in special:
        return special[s]
    if len(s) == 2:
        return '{}-{}'.format(special[s[0] + '0'], special[s[1]])
    else:
        lower2 = three_digits2words(s[1:])
        return '{} hundred'.format(special[s[0]]) + (' ' + lower2 if lower2 != 'zero' else '')


def number2words(n):
    """ works for numbers between 0 and 999999 """
    s = str(n)
    lower3 = three_digits2words(s[-3:])
    if len(s) > 3:
        return '{} thousand'.format(three_digits2words(s[:-3])) + (' ' + lower3 if lower3 != 'zero' else '')
    else:
        return lower3
