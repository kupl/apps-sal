def chromosome_check(sperm: str) -> str:
    """ Determine if the sex of the offspring based on the X or Y chromosome present in the male's sperm. """
    return f"Congratulations! You're going to have a {('son' if sperm == 'XY' else 'daughter')}."
