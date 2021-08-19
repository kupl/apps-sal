def run_length_encoding(s):
    if len(s) == 0:
        return []
    encoded_s = [[1, s[0]]]
    last_char = s[0]
    for char in s[1:]:
        if char == last_char:
            encoded_s[-1][0] = encoded_s[-1][0] + 1
        else:
            encoded_s.append([1, char])
        last_char = char
    return encoded_s
