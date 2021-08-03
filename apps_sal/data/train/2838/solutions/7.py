def char_concat(word):
    return ''.join(('%s%s%d' % (a, b, i)) for (i, (a, b)) in enumerate(zip(word[:len(word) // 2], reversed(word[-len(word) // 2:])), 1))
