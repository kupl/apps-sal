def alphabet_war(fight):
    lefts, rights = ('wpbs', 'mqdz')
    score_right = sum([4 - rights.find(x) for x in fight if x in rights])
    score_left = sum([4 - lefts.find(x) for x in fight if x in lefts])
    return ['Let\'s fight again!', ['Right side wins!', 'Left side wins!'][score_left > score_right]][score_right != score_left]

