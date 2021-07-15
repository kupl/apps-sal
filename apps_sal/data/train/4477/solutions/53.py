def reverse_number(n):
    s = str(abs(n))
    result = int(s[::-1])
    return result if n >=0 else -1*result

