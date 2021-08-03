def did_we_win(plays):
    s = 0
    for i in range(4):
        if not plays[i]:
            break
        if plays[i][1] == "turnover":
            return False
        s += plays[i][0] * (-1)**(plays[i][1] == "sack")
    return s > 10
