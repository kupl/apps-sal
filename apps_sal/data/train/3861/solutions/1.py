def fire_and_fury(tweet):
    if not all(c in 'EFIRUY' for c in tweet):
        return 'Fake tweet.'
    s = [0]
    for i in range(0, len(tweet) - 3):
        if tweet[i:i + 4] == 'FIRE':
            if s[-1] > 0:
                s[-1] += 1
            else:
                s.append(1)
        elif tweet[i:i + 4] == 'FURY':
            if s[-1] < 0:
                s[-1] -= 1
            else:
                s.append(-1)
    return 'Fake tweet.' if len(s) == 1 else ' '.join(['You' + ' and you' * (s[i] - 1) + ' are fired!' if s[i] > 0 else 'I am' + ' really' * (-s[i] - 1) + ' furious.' for i in range(1, len(s))])
