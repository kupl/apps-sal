def elevator(left: int, right: int, call: int) -> str:
    """ Get the name of the elevator closest to the called floor ("left"/"right"). """
    return "left" if abs(right - call) > abs(left - call) else "right" if abs(right - call) < abs(left - call) else "right"
