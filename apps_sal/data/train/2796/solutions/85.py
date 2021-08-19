def areYouPlayingBanjo(name):
    return f"{name} {('plays' if name.lower().startswith('r') else 'does not play')} banjo"
