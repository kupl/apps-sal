def playerRankUp(player_points):
    if player_points < 100:
        return False
    else:
        return f'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'
