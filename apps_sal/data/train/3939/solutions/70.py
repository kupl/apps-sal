def rps(p1, p2):
    if p1 == 'scissors' and p2 == 'paper':
        resultado = "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'rock':
        resultado = "Player 2 won!"
    elif p1 == 'paper' and p2 == 'rock':
        resultado = "Player 1 won!"
    elif p1 == 'paper' and p2 == 'scissors':
        resultado = "Player 2 won!"
    elif p1 == 'rock' and p2 == 'paper':
        resultado = "Player 2 won!"
    elif p1 == 'rock' and p2 == 'scissors':
        resultado = "Player 1 won!"
    else:
        resultado = "Draw!"
    return resultado
