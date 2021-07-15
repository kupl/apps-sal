def areYouPlayingBanjo(name: str) -> str:
    """ Check if the user is playing banjo based on his name. """
    return name + " plays banjo" if name.lower().startswith("r") else name + " does not play banjo"
