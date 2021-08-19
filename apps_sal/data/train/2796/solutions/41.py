def areYouPlayingBanjo(name):
    # Implement me!
    return ['{} does not play banjo'.format(name), '{} plays banjo'.format(name)][name[0].lower() == 'r']
