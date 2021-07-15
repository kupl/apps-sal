def words_to_marks(s):
    letters = map(chr, range(97, 123))
    integers = range(1, 27)
    definition = dict(zip(letters, integers))
    result = 0
    for i in s:
        result += definition.get(i, 0)
    return result
