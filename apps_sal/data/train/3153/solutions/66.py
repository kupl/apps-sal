def playerRankUp(pts):
    # your code here
    msg_str = "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
    return msg_str if pts >= 100 else False
