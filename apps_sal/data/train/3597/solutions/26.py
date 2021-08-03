def say_hello(name, city, state):
    lis = []
    lis.append("Hello,")
    lis.append(" ".join(name) + "!")
    lis.append("Welcome to")
    lis.append(city + ",")
    lis.append(state + "!")
    return " ".join(lis)
