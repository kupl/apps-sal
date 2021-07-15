def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    rock_sciss = p1=="rock" and p2=="scissors"
    paper_rock = p1=="paper" and p2=="rock"
    sciss_paper = p1=="scissors" and p2=="paper"
    
    if rock_sciss or paper_rock or sciss_paper:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
