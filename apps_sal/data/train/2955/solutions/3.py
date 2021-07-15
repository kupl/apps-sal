def oddest(a):
    return max(a, key=lambda n: f'{n+2**32:b}'[::-1])
