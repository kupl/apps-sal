def get_participants(handshakes):
    farmers = 1
    maxshakes = 0
    while maxshakes < handshakes:
        maxshakes += farmers
        farmers += 1
    return farmers
