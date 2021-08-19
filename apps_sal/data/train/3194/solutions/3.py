def berserk_rater(synopsis):
    ball = 0
    ball = sum([ball + 5 if 'clang' in i.lower() else ball - 2 if 'cg' in i.lower() else ball - 1 for i in synopsis])
    return 'worstest episode ever' if ball < 0 else str(ball) if ball <= 10 else 'bestest episode ever'
