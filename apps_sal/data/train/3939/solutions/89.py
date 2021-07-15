def rps(p1, p2):
    return {
        p1=='rock' and p2=='scissors' or p1=='paper' and p2=='rock' or p1=='scissors' and p2=='paper' : 'Player 1 won!', p1==p2:'Draw!'
    }.get(1,'Player 2 won!')
