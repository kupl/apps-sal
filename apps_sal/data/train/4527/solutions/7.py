def winner(deck_steve, deck_josh):
    deck  = [deck_steve, deck_josh]
    score = [e[1]>e[0] for e in zip( *[map('23456789TJQKA'.index, x) 
                       for x in deck ]) if e[1]!=e[0] ]
    l,s,f = len(score)/2, sum(score), score.count(False)
    winer = [('Steve',f,s),('Josh',s,f)][s>l]
    return 'Tie' if not score or s==l else '{} wins {} to {}'.format( *winer )
