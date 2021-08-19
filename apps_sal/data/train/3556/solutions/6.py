def diamonds_and_toads(s, f):
    return {'ruby': s.count('r') + s.count('R') * 2, 'crystal': s.count('c') + s.count('C') * 2} if f == 'good' else {'python': s.count('p') + s.count('P') * 2, 'squirrel': s.count('s') + s.count('S') * 2}
