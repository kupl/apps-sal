def hero(bullets,dragons) :
    x=int(dragons)*2
    if int(bullets)<int(x) :
        return False
    elif int(bullets)>=int(x) :
        return True

