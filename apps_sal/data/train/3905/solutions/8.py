def missing(s):

    def missing(s, base, candidate=-1):
        (head, tail) = (int(s[:base]), s[base:])
        if tail.startswith(str(head + 1)):
            return missing(tail, len(str(head + 1)), candidate)
        if tail.startswith(str(head + 2)):
            return missing(tail, len(str(head + 2)), head + 1) if candidate == -1 else -1
        return candidate if tail == '' else -1
    for base in range(1, len(s) // 2 + 1):
        result = missing(s, base)
        if result != -1:
            return result
    return -1
