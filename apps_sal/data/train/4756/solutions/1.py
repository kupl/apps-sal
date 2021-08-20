import re
cons = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowels = 'AEIOUaeiou'


def __starting_point():
    string = input().strip()
    m = re.findall('(?<=[%s])([%s]{2,})[%s]' % (cons, vowels, cons), string)
    print('\n'.join(m or ['-1']))


__starting_point()
