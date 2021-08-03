def insert_missing_letters(st):
    az = [chr(a) for a in (list(range(ord('a'), ord('z') + 1)))]
    return ''.join([st[i] + ''.join([a.upper() for a in az[az.index(st[i]) + 1:] if a not in st]) if st[i] not in st[:i] else st[i] for i in range(len(st))])
