def greet(name):
    greeting = ''
    if name == 'Johnny':
        greeting = 'Hello, my love!'
    else:
        greeting = 'Hello, ' + name + '!'
    return greeting


print(greet('Maria'))
print(greet('Johnny'))
