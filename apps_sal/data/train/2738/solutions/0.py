def i_tri(s):
    total = 2.4 + 112 + 26.2
    to_go = '%.2f to go!' % (total - s)

    return ('Starting Line... Good Luck!' if s == 0 else
            {'Swim': to_go} if s < 2.4 else
            {'Bike': to_go} if s < 2.4 + 112 else
            {'Run': to_go} if s < total - 10 else
            {'Run': 'Nearly there!'} if s < total else
            "You're done! Stop running!")
