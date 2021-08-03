def rps(p1, p2):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    p1won = "Player 1 won!"
    p2won = "Player 2 won!"
    draw = 'Draw!'
    solutions = {rock: {rock: draw,
                        paper: p2won,
                        scissors: p1won, },
                 paper: {rock: p1won,
                         paper: draw,
                         scissors: p2won, },
                 scissors: {rock: p2won,
                            paper: p1won,
                            scissors: draw, }, }
    return solutions[p1][p2]
