def run_length_encoding(string):
    code = []
    for c in string:
        if not code or code[-1][1] != c:
            code.append([1, c])
        else:
            code[-1][0] += 1
    return code
