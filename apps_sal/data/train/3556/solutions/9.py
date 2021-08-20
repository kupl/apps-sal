def diamonds_and_toads(sentence, fairy):
    if fairy == 'good':
        return {'ruby': sentence.count('r') + 2 * sentence.count('R'), 'crystal': sentence.count('c') + 2 * sentence.count('C')}
    return {'python': sentence.count('p') + 2 * sentence.count('P'), 'squirrel': sentence.count('s') + 2 * sentence.count('S')}
