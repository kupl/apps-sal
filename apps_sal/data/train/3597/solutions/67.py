def say_hello(name, city, state):
    full_name = ""
    for i in name:
        full_name += f" {i}"
    return f"Hello,{full_name}! Welcome to {city}, {state}!"
