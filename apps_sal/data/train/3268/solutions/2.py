def words_to_object(s):
    words = s.split()

    res = []

    for key in range(0, len(words) - 1, 2):
        value = key + 1

        res.append("{name : " + "'" + words[key] + "'" + ", " + "id : " + "'" + words[value] + "'}")

    return "[" + ", ".join(res) + "]"
