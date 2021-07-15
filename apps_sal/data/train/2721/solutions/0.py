def pyramid(n):
    return '\n'.join("/{}\\".format(" _"[r==n-1] * r*2).center(2*n).rstrip() for r in range(n)) + '\n'
