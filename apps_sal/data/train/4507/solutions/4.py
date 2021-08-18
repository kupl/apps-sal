def endless_string(strng, start, length):
    len_strng = len(strng)
    strng = strng * (abs(length) // len_strng + 1)
    true_start = min(start, start + length)
    start = true_start % len_strng + (length < 0)
    stop = start + abs(length)
    return strng[start:stop]
