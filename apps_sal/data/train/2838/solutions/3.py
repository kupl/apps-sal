def char_concat(word):
    half = len(word) // 2
    return ''.join('{}{}{}'.format(a[0], a[1], i) for i, a in enumerate(zip(word[:half], word[::-1][:half]), 1))
