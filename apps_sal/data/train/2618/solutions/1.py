import re


def __starting_point():
    t = int(input().strip())
    for _ in range(t):
        uid = ''.join(sorted(input()))
        if len(uid) == 10 and re.match('', uid) and re.search('[A-Z]{2}', uid) and re.search('\\d\\d\\d', uid) and (not re.search('[^a-zA-Z0-9]', uid)) and (not re.search('(.)\\1', uid)):
            print('Valid')
        else:
            print('Invalid')


__starting_point()
