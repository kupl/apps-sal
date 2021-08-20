def oracle(a):
    return '\n'.join(('----%s----' % 'x- o'[i.count('h')] for i in sorted(a, key=lambda x: -ord(x[0][2]))))
