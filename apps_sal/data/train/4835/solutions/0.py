SCORE = {'O': '0', 'o': '0', 'k': '1'}


def okkOokOo(s):
    return ''.join((chr(int(''.join((SCORE.get(a, '') for a in word)), 2)) for word in s.split('?')))
