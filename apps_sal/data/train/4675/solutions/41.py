def set_alarm(employed, vacation):
    return False if not employed and vacation else employed ^ vacation
