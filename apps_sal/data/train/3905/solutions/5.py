def missing(s):
    for i in range(1, len(s) // 2 + 1):
        (n, missing) = (int(s[:i]), None)
        while i < len(s):
            n += 1
            j = len(str(n))
            if s.startswith(str(n)[:len(s) - i], i):
                i += j
            elif missing:
                missing = None
                break
            else:
                missing = n
        else:
            if not missing:
                return -1
        if missing:
            return missing
    return -1
