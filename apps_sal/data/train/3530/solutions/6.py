def asterisc_it(n):
    asterisk_str = ""
    if type(n) == int:
        n = str(n)
    elif type(n) == list:
        n = ''.join(map(str, n))

    for i, j in enumerate(range(1, len(n))):
        asterisk_str += n[i]
        print(i, j)
        if int(n[i]) % 2 == 0 and int(n[j]) % 2 == 0:
            asterisk_str += "*"

    return asterisk_str + n[-1]
