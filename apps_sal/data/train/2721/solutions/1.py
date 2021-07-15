def pyramid(n):
    return '\n'.join(('/%s\\' % (' _'[i == n-1] * i*2)).rjust(n+i+1) for i in range(n)) + '\n'
