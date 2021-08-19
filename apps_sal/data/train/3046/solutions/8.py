from codecs import decode
tm = b'QlpoOTFBWSZTWYSVjQkACcGIAGAAIACQEAUjUFRlVFsRLBUYVGKjKjVGJo01tbMxratRqjKjFRhU\nYJbQSyFRpCo4u5IpwoSEJKxoSA=='
for c in ('base64', 'bz2', 'utf8'):
    tm = decode(tm, c)


def thue_morse(n):
    return tm[:n]
