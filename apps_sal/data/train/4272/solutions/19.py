def greet(name):
    """ Jenny was all hyped by the possibillity Johnny might check her web app
    so she made a mistake by returning the result before checking if Johnny
    is one of the users logging to her web app. Silly girl!
    We corrected the function by adding an else statement."""
    if name == 'Johnny':
        return 'Hello, my love!'
    else:
        return 'Hello, {name}!'.format(name=name)
