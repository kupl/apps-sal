def stringy(size):
    choices = [1, 0]
    a = ''
    for i in range(size):
        a += str(choices[i % 2])
    return a
