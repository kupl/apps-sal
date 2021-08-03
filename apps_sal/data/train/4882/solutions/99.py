def round_to_next5(n):
    if n % 5 == 0:
        return n
    if n % 5 != 0:
        n = n + 4
        if n % 5 != 0:
            n = n - 1
            if n % 5 != 0:
                n = n - 1
                if n % 5 != 0:
                    n = n - 1
                    if n % 5 != 0:
                        n = n - 1
                    elif n % 5 == 0:
                        return n
                elif n % 5 == 0:
                    return n
            elif n % 5 == 0:
                return n
        elif n % 5 == 0:
            return n
