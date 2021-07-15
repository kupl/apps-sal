def areYouPlayingBanjo(name):
    return name+([' does not play',' plays'][name.lower().startswith('r')])+' banjo'
