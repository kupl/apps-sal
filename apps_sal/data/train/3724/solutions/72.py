def hero(bullets, dragons):
    print(('bullets are {} and dragons are {}'.format(bullets,dragons)))
    if bullets < 2:
        return False
    
    bulletsNeeded = dragons * 2
    
    if bullets - bulletsNeeded >= 0:
        return True
    else:
        return False

