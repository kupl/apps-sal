def i_tri(s):
    if s == 0:
        return 'Starting Line... Good Luck!'
    if s < 2.4:
        return {'Swim': f'{140.6 - s:.2f} to go!'}
    if s < 114.4:
        return {'Bike': f'{140.6 - s:.2f} to go!'}
    if s < 130.6:
        return {'Run': f'{140.6 - s:.2f} to go!'}
    if s < 140.6:
        return {'Run': 'Nearly there!'}
    return "You're done! Stop running!"
