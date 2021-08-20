def playerRankUp(pts):
    congrat = 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'
    return congrat if pts >= 100 else False
