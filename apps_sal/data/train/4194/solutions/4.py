def next_version(version):
    lst = list(map(int, version.split('.')))
    for i in reversed(range(len(lst))):
        lst[i] += 1
        if i:      lst[i] %= 10
        if lst[i]: break
    return '.'.join(map(str, lst))
