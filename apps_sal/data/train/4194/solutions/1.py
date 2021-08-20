def next_version(version):
    tab = list(map(int, version.split('.')))
    for x in range(1, len(tab) + 1):
        if tab[-x] is 9 and x != len(tab):
            tab[-x] = 0
        else:
            tab[-x] += 1
            break
    return '.'.join(list(map(str, tab)))
