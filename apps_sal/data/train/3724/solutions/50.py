def hero(bullets, dragons):
    while True:
        bullets -= 2
        dragons -= 1
        if bullets >= 0 and dragons == 0:
            return True
        elif bullets < 0 or dragons < 0:
            return False
