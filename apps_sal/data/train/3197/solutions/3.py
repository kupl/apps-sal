def conjugate(verb):
    (root, oldSuffix) = (verb[:-2], verb[-2:])
    newSuffix = {'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'], 'er': ['o', 'es', 'e', 'emos', 'eis', 'en'], 'ir': ['o', 'es', 'e', 'imos', 'is', 'en']}
    answer = {verb: []}
    for ns in newSuffix[oldSuffix]:
        answer[verb].append(root + ns)
    return answer
