def hero(bullets, dragons):
    print(bullets, dragons)
    hm = bullets / 2
    print(hm)
    if hm >= dragons:
        return True
    else:
        return False
