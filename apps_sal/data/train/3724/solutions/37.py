def hero(bullets, dragons):

    try:

        devide = bullets // dragons

    except:
        pass

    if devide >= 2:

        return True

    else:

        return False


hero(10, 5)
