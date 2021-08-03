def trotter(n):
    seek = {str(e) for e in range(10)}
    for k in range(1, 73):
        seek -= {e for e in str(n * k)}
        if not seek:
            return n * k
    return 'INSOMNIA'
