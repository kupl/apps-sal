import string


def words_to_marks(s):
    result = []
    counter = dict(zip(string.ascii_lowercase, range(1, 27)))
    for i in s:
        if i in counter.keys():
            result.append(counter.get(i))
    return sum(result)
