def rps(p1, p2):
    if p1 == p2: return "Draw!"
    dic = {"rs": 1, "sp": 1, "ps": 2, "sr": 2, "pr": 1, "rp": 2}
    return f"Player {dic[p1[0] + p2[0]]} won!"
