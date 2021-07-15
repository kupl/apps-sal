def next_bigger(n):
    i, ss = n, sorted(str(n))

    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1;

    while True:
        i += 1;
        if sorted(str(i)) == ss and i != n:
            return i;

