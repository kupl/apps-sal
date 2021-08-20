def create_phone_number(n):
    n = list(map(str, n))
    return '({}) {}-{}'.format(''.join(n[:3]), ''.join(n[3:6]), ''.join(n[6:10]))
