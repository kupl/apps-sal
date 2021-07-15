def rps(p1, p2):
    d = {("rock","scissors"):"Player 1 won!",
         ("paper","scissors"):"Player 2 won!",
         ("paper","rock"):"Player 1 won!",
         ("scissors","rock"):"Player 2 won!",
         ("scissors","paper"):"Player 1 won!",
         ("rock","paper"):"Player 2 won!",
         ("paper","paper"):"Draw!",
         ("rock","rock"):"Draw!",
         ("scissors","scissors"):"Draw!",}
    if (p1,p2) in d:
        return d[(p1,p2)]
