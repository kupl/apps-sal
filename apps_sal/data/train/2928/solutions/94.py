def alphabet_war(fight):
    versus = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    score = []
    for x in fight:
        for key, value in versus.items():
            if x == key:
                score.append(value)
    if sum(score) > 0:
        return 'Left side wins!'
    if sum(score) < 0:
        return 'Right side wins!'
    return "Let's fight again!"
    
print(alphabet_war('zzzzs'))
