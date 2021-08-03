def say_hello(name, city, state):
    greeting = "Hello, {name}! Welcome to {city}, {state}!".format(
        name=" ".join(name),
        city=city,
        state=state
    )

    return greeting
