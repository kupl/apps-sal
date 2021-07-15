def jumbled_string(s, n):
    results = [s]
    while n:
        s = s[::2] + s[1::2]
        n -= 1
        if s == results[0]:
            return results[n % len(results)]
        else:
            results.append(s)
    return s
