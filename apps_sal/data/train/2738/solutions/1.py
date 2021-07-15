def i_tri(s):
    remain = 2.4 + 112 + 26.2 - s
    if s == 0:
        return 'Starting Line... Good Luck!'
    elif s < 2.4:
        return {'Swim': f'{remain:.2f} to go!'}
    elif s < 2.4 + 112:
        return {'Bike': f'{remain:.2f} to go!'}
    elif remain > 10:
        return {'Run': f'{remain:.2f} to go!'}
    elif remain > 0:
        return {'Run': 'Nearly there!'}
    else:
        return "You're done! Stop running!"
