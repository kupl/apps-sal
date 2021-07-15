def next_version(version):
    vs = list(map(int, version.split('.')))
    for i in range(len(vs)-1, -1, -1):
        vs[i] += 1
        if vs[i] < 10:
            break
        if i:
            vs[i] %= 10
    return '.'.join(map(str, vs))
