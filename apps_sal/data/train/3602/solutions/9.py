def run_length_encoding(s):
    result = []
    if s:
        prev = s[0]
        count = 1
        for ind in range(1, len(s)):
            if s[ind] == prev:
                count += 1
            else:
                result.append([count, prev])
                prev = s[ind]
                count = 1
        result.append([count, prev])
    return result
