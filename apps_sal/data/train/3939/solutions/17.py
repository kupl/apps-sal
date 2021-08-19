def rps(p1, p2):
    nums = ['rock', 'scissors', 'paper']
    p1 = nums.index(p1)
    p2 = nums.index(p2)
    if p1 == p2:
        return 'Draw!'
    elif (p2 - p1) % 3 == 1:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
