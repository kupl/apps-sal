def hero(bullets, dragons):
    shots = bullets // 2
    if shots >= dragons:
        return True
    else:
        return False
