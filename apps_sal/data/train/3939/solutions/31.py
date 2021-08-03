def rps(p1, p2):
    res = ("rsp".find(p2[0]) - "rsp".find(p1[0])) % 3
    return f"Player {res} won!" if res else "Draw!"
