def hello(name="World"):
    if name == '':
        return 'Hello, World!'
    else:
        name = name.capitalize()
        return 'Hello, %s!' % (name)


print((hello('John')))
print((hello('aLIce')))
print((hello()))
print((hello("")))
