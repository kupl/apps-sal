def berserk_rater(synopsis):
    scores = []
    for sentence in synopsis:
        # Remove punctuation
        s = ''.join([c for c in sentence.lower() if c == ' ' or c.isalpha() or c.isdigit()])
        words = s.split()
        # Count the appropriate words
        cg = words.count('cg')
        clang = sum(1 for w in words if w.startswith('clang'))
        # Decide sentence scoore
        if clang:
            scores.append(5)
        elif cg:
            scores.append(-2)
        else:
            scores.append(-1)

    score = sum(scores)
    # Decode overall score
    if score < 0:
        return 'worstest episode ever'
    if score > 10:
        return 'bestest episode ever'
    return str(score)
