def say_hello(name, city, state):
    word = "Hello, "
    for i in name:
        word += str(i) + " "
    result = word[:-1]
    result += "! Welcome to " + str(city) + ", " + str(state) + "!"
    return result
