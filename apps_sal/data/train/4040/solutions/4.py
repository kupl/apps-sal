def nth_char(words):
    return ''.join((words[n][n] for n in range(len(words))))
