def greet(name, owner):
    statement = 'Hello '
    if name == owner:
        statement += 'boss'
    else:
        statement += 'guest'
    return statement
