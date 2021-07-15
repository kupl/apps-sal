def run_length_encoding(s):
    result = []
    i = j = 0
    while i < len(s):
        while j < len(s) and s[i] == s[j]:
            j += 1
        result.append([j-i, s[i]])
        i = j
    return result
