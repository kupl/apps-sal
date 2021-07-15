def caesar_crypto_encode(s, n):
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r = ''
    for i in s or '':
        if i in a:
            r += a[(a.index(i) + n) % 52]
        else:
            r += i
    return r.strip()
