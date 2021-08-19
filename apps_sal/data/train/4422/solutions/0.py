def jumbled_string(s, n):
    iterations = [s]
    while True:
        s = s[::2] + s[1::2]
        if s == iterations[0]:
            break
        iterations.append(s)
    return iterations[n % len(iterations)]
