def diamonds_and_toads(phrase, fairy):
    if fairy == 'good':
        return {'ruby': phrase.count('r') + phrase.count('R') * 2, 'crystal': phrase.count('c') + phrase.count('C') * 2}
    else:
        return {'python': phrase.count('p') + phrase.count('P') * 2, 'squirrel': phrase.count('s') + phrase.count('S') * 2}
