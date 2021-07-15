def hero(bullets, dragons):
    for i in range(dragons):
        bullets -= 2
    return bullets >= 0
