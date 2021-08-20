strokes = {c: str(i) for (i, s) in enumerate(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'], 2) for c in s}


def unlock(message):
    return ''.join(map(strokes.get, message.lower()))
