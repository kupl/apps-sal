def say_hello(name, city, state):
    nam = ''
    if len(name) == 2:
        nam = name[0] + ' ' + name[1]
    elif len(name) == 3:
        nam = name[0] + ' ' + name[1] + ' ' + name[2]
    elif len(name) == 4:
        nam = name[0] + ' ' + name[1] + ' ' + name[2] + ' ' + name[3]
    elif len(name) == 5:
        nam = name[0] + ' ' + name[1] + ' ' + name[2] + ' ' + name[3] + ' ' + name[4]

    return f"Hello, {nam}! Welcome to {city}, {state}!"
