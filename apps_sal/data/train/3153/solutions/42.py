def playerRankUp(pts):
    # your code here
    a = (pts - 100) // 100
    if a < 0:
        return False
    else:
        return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
