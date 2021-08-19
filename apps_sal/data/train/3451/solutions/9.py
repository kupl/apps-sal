def triangle(row):
    vector = list(row)
    while len(vector) > 1:
        vector = [((set('RGB') - {a, b}).pop(), a)[a == b] for (a, b) in zip(vector, vector[1:])]
    return vector[0]
