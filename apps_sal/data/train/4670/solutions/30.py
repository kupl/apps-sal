def string_to_number(s):
    result = 0
    for i in range(len(s)):
        result = result * 10 + int(s[i]) if s[i] in '0123456789' else result
    return -result if s[0] == '-' else result
