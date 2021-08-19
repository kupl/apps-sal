def greet(name):
    greetings = ['Hello,', 'how', 'are', 'you', 'doing', 'today?']
    greetings.insert(1, str(name))
    return lista_to_string(greetings)


def lista_to_string(L):
    return ' '.join((str(x) for x in L))
