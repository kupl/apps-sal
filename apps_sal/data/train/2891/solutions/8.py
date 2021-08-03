from string import ascii_lowercase as letters


def find_the_key(message, code):
    diff = [e - letters.index(c) - 1 for (e, c) in zip(code, message)]
    for n in range(1, len(diff)):
        ok = True
        for k in range(n, len(diff), n):
            if diff[k:k + n] != diff[:min(n, len(diff) - k)]:
                ok = False
                break
        if ok:
            diff = diff[:n]
            break
    key = 0
    for k in diff:
        key = key * 10 + k
    return key
