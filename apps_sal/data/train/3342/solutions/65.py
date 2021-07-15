def pattern(n):
    if n<1:
        return ''
    return '\n'.join((elem*str(elem))for elem in range(1,n+1))

