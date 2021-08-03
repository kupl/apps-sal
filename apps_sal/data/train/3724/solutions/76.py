def hero(bullets, dragons):
    kills = bullets / 2
    print(kills, dragons)
    if dragons > kills:
        return False
    if dragons <= kills:
        return True
