def greet(name, owner):
    return ("Hello boss", "Hello guest")[name != owner]
