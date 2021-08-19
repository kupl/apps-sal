def rps(p1, p2):
    dict = {'rock': 0, 'paper': 1, 'scissors': 2}
    gameover = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return gameover[(dict[p1] + -dict[p2]) % 3]
