def say_hello(name, city, state):
    x = "Hello, {}! Welcome to " + city + ", " + state + "!"
    temp = ""
    for i in name:
        temp+=i+" "
    temp = temp[:-1]
    z = x.format(temp)
    return z
