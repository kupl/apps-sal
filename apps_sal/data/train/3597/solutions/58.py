def say_hello(name, city, state):
    str_name = ' '.join(name)
    return "Hello, {str_name}! Welcome to {city}, {state}!".format(str_name=str_name, city=city, state=state)


print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))
