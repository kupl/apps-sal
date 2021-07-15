def hamster_me(code, message):
    cache = {k:k+"1" for k in code}
    for l in code:
        for i in range(2, 27):
            shifted = chr(97 + (ord(l) - 98 + i) % 26)
            if shifted in cache:
                break
            cache[shifted] = l + str(i)
    return "".join(map(lambda x: cache[x], message))
