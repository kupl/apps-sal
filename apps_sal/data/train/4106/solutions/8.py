def rec(n, seen):
    if n == '0' * len(n):
        return -1
    seen.add(n)
    res = str(int(''.join(sorted(n, reverse=True))) - int(''.join(sorted(n)))).zfill(len(n))
    if res in seen:
        return len(seen)
    return rec(res, seen)


def self_converge(number):
    return rec(str(number), set())
