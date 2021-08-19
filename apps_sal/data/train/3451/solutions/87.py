def compare(pair):
    if len(set(pair)) == 1:
        return pair[0]
    return list(set(pair) ^ set('RGB'))[0]


def triangle(row):
    return triangle([compare([row[i], row[i + 1]]) for i in range(len(row) - 1)]) if len(row) > 1 else row[0]
