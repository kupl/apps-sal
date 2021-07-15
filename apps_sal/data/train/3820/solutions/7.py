def checkered_board(n):
    if type(n) is not int or n <2: return False
    return '\n'.join(map(lambda i: ' '.join(map(lambda j: '□' if ((n-j) + i) % 2 == 0 else '■', range(n))), range(n)))
