def counting_valleys(walk):
    level, valleys = 0, 0
    for step in walk:
        valleys += (level == -1) and (step == "U")
        level += (step == "U") or -(step == "D")
    return valleys
