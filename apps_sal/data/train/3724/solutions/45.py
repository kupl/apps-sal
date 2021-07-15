bullets = [*range(0, 10)]
dragons = [*range(0, 10)]
def hero(bullets, dragons):
    if bullets / dragons >= 2:
        return True
    else: return False
