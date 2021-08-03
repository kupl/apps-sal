def hello(name='World'):
    if(name == '' or name == 'World'):
        return 'Hello, World!'
    output = name.lower()
    output = output.split()
    output2 = output[(len(output) - 1)]
    return 'Hello, ' + output2.capitalize() + '!'
