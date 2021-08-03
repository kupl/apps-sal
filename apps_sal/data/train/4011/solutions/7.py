def get_free_urinals(urinals):
    return -1 if "11" in urinals else sum(len(x) - 1 >> 1 for x in f"0{urinals}0".split('1'))
