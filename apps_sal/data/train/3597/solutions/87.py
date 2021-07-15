def say_hello(name, city, state):
    a = ''
    for x in range(0,len(name)):
        a = a + ' ' + ''.join(name[x])
    return 'Hello, ' + a[1:] + '! Welcome to ' + city + ', ' + state + '!' 
    

