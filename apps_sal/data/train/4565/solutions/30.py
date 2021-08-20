def replace_dots(s):
    return ''.join(['-' if c == '.' else c for c in s])
