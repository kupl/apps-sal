def oddity(n):
    counter = 0
    for x in range(1, int(n**.5) + 1):
        a, b = divmod(n, x)
        if not b:
            if a != x:
                counter += 2
            else:
                counter += 1
    return ('even', 'odd')[counter % 2]
