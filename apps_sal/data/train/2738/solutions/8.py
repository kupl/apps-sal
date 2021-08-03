def i_tri(s):
    return 'You\'re done! Stop running!' if s >= 140.6 \
        else {'Run': 'Nearly there!'} if s >= 130.6 \
        else {'Run': '{0:.2f} to go!'.format(140.6 - s)} if s >= 114.4 \
        else {'Bike': '{0:.2f} to go!'.format(140.6 - s)} if s >= 2.4 \
        else {'Swim': '{0:.2f} to go!'.format(140.6 - s)} if s > 0 \
        else 'Starting Line... Good Luck!'
