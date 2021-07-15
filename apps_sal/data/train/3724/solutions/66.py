def hero(bullets, dragons):
    try:
        return bullets // dragons >= 2
    except ZeroDivisionError:
        return True
