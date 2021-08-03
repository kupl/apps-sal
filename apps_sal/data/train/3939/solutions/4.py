RPS = {('rock', 'rock'): 'Draw!',
       ('rock', 'paper'): 'Player 2 won!',
       ('rock', 'scissors'): 'Player 1 won!',
       ('paper', 'rock'): 'Player 1 won!',
       ('paper', 'paper'): 'Draw!',
       ('paper', 'scissors'): 'Player 2 won!',
       ('scissors', 'rock'): 'Player 2 won!',
       ('scissors', 'paper'): 'Player 1 won!',
       ('scissors', 'scissors'): 'Draw!'}


def rps(p1, p2):
    return RPS[(p1, p2)]
