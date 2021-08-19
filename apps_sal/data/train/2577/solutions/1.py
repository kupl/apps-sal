import re


def __starting_point():
    t = int(input().strip())
    for _ in range(t):
        num = ''.join(input())
        if re.match('^[456]', num) and (re.match('([\\d]{4}-){3}[\\d]{4}$', num) or re.match('[\\d]{16}', num)) and (not re.search('(\\d)\\1{3,}', num.replace('-', ''))):
            print('Valid')
        else:
            print('Invalid')


__starting_point()
