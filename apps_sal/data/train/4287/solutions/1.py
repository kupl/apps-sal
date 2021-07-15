def get_participants(handshakes, n = 1):
    return get_participants(handshakes, n + 1) if (n * n - n)/2 < handshakes else n
