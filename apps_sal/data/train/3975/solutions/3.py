def find_missing_letter(chars):
    for x in range(1, len(chars)):
        if ord(chars[x]) - ord(chars[x - 1]) != 1:
            return chr(ord(chars[x]) - 1)
