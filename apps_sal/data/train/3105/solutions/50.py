def count_sheep(n):
    thing = ''
    for i in range(1, n + 1):

        thing += str(i)
        thing += " sheep..."
    return thing
