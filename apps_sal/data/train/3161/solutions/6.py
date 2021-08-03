def select(memory):

    def records(tokens):
        for token in tokens:
            if token.startswith('!'):
                yield token[1:], True
            else:
                yield token, False

    def contagious(records):
        mark_next = False
        for name, marked in records:
            if mark_next:
                yield name, True
            else:
                yield name, marked
            mark_next = marked

    separator = ', '
    tokens = memory.split(separator)
    recordset = list(contagious(records(tokens)))

    hated = set(name for name, marked in recordset if marked)
    loved = (name for name, _ in recordset if name not in hated)
    return separator.join(loved)
