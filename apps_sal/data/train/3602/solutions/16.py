def run_length_encoding(s):
    if len(s) == 0:
        return []

    encoded_s = [[1, s[0]]]
    last_char = s[0]

    for char in s[1:]:
        if char == last_char:
            # increment running count
            encoded_s[-1][0] = encoded_s[-1][0] + 1
        else:
            # start counting new char
            encoded_s.append([1, char])
        # update last_char getting ready for next time through the loop
        last_char = char

    return encoded_s
