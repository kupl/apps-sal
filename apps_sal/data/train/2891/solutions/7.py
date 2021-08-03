def find_the_key(message, code):
    # your code here
    import string
    mapowanie_str_dig = dict(zip(list(string.ascii_lowercase), [x for x in range(1, 27)]))
    m = []
    for s in message:
        m = m + [mapowanie_str_dig[s]]
    delta = [str(abs(code[i] - m[i])) for i in range(0, len(m))]
    for i in range(1, len(delta) + 1):
        n = len(delta) // i
        r = len(delta) % i
        if n * delta[0:i] == delta[0:n * i] and delta[0:r] == delta[n * i:]:
            output = delta[0:i]
            break
    return int(''.join(output))
