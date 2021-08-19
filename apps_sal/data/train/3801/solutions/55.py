import string
values = dict()
for (index, letter) in enumerate(string.ascii_lowercase):
    values[letter] = index + 1


def words_to_marks(s):
    total = 0
    for let in s:
        total += values[let]
    return total
