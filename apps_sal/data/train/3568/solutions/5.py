def bumps(road):
    MAX_BUMPS = 15
    SUCCESS_MESSAGE = 'Woohoo!'
    ERROR_MESSAGE = 'Car Dead'

    return SUCCESS_MESSAGE if road.count('n') <= MAX_BUMPS else ERROR_MESSAGE
