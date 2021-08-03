def create_phone_number(n):
    n = ''.join(map(str, n))
    return '(%s) %s-%s' % (n[:3], n[3:6], n[6:])
