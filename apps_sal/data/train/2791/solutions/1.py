def trigrams(phrase):
    solution = ''
    if len(phrase) < 3:
        return solution
    phrase = phrase.replace(' ', '_')
    for i in range(len(phrase) - 2):
        solution = solution + ' ' + phrase[i:i + 3]
    return solution[1:]
