def next_version(version):
    (carry, minors) = (1, [])
    for (i, n) in list(enumerate(version.split('.')))[::-1]:
        (carry, n) = divmod(int(n) + carry, 10 if i else int(n) + 2)
        minors.append(str(n))
    return '.'.join(minors[::-1])
