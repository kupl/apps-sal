def diamonds_and_toads(sentence, fairy):
    res = {}
    if fairy == 'good':
        res['ruby'] = sentence.count('r') + sentence.count('R') * 2
        res['crystal'] = sentence.count('c') + sentence.count('C') * 2
    elif fairy == 'evil':
        res['python'] = sentence.count('p') + sentence.count('P') * 2
        res['squirrel'] = sentence.count('s') + sentence.count('S') * 2
    return res
