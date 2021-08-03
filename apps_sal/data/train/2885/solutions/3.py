def champernowneDigit(n):

    result = float("NaN")
    if type(n) == int and n > 0:
        if n <= 10:
            result = n - 1
        else:
            i = 1
            c = 10
            while n > c:
                i += 1
                c = c + i * 9 * 10**(i - 1)

            number = (n - c) // i + 10**i - 1
            reste = (n - c) % i
            if reste:
                number += 1
            result = int(str(number)[reste - 1])
    return result
