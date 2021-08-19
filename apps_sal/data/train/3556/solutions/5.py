def diamonds_and_toads(sentence, fairy):
    if fairy == 'good':
        return {'ruby': sentence.count('r') + sentence.count('R') * 2, 'crystal': sentence.count('c') + sentence.count('C') * 2}
    else:
        return {'python': sentence.count('p') + sentence.count('P') * 2, 'squirrel': sentence.count('s') + sentence.count('S') * 2}
