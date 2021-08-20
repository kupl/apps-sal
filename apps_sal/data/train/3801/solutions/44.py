def words_to_marks(s):
    import string
    a = string.ascii_lowercase[:]
    b = list(range(1, len(a) + 1))
    dictionary = {}
    i = 0
    for x in a:
        dictionary[x] = b[i]
        i += 1
    new_list = []
    for x in s:
        new_list.append(dictionary.get(x))
    return sum(new_list)
