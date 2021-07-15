def hello(name=''):
    if len(name) == 0:
        return 'Hello, World!'
    ls = list(name)
    word = True
    for i in range(len(ls)):
        word = word and ls[i].isalpha()
    if word == True:
        return 'Hello, ' + name[0].upper() + name[1:].lower() + '!'





