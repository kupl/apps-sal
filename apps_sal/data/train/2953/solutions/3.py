def numericals(s):
    history = {}
    result = []
    for char in s:
        if char not in history:
            history[char] = 1
        else:
            history[char] += 1
        result.append(history[char])
    return ''.join(map(str, result))
