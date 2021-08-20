def string_counter(string, char):
    if char not in string:
        return 0
    c = string[0]
    if c == char:
        return 1 + string_counter(string[1:], char)
    return string_counter(string[1:], char)


print(string_counter('Hello World', 'o'))
