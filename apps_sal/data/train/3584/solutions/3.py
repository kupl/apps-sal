rs = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm,.', 'QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM<>')


def encrypt(t, k):
    k = [k // 100, k // 10 % 10, k % 10]
    return t.translate(str.maketrans(''.join(rs), ''.join((rs[i][k[i % 3]:] + rs[i][:k[i % 3]] for (i, r) in enumerate(rs)))))


def decrypt(t, k):
    k = [k // 100, k // 10 % 10, k % 10]
    return t.translate(str.maketrans(''.join(rs), ''.join((rs[i][-k[i % 3]:] + rs[i][:-k[i % 3]] for (i, r) in enumerate(rs)))))
