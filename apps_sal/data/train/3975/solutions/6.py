def find_missing_letter(chars):
    for i in range(0, len(chars) - 1):
        current = chars[i]
        after = chars[i + 1]
        expected = chr(ord(current) + 1)
        if after != expected:
            return expected
    return ''
