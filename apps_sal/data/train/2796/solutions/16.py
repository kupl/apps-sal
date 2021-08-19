def areYouPlayingBanjo(name):
    return ['%s plays banjo' % name, '%s does not play banjo' % name][name[0].lower() != 'r']
