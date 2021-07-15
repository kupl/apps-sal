def greet(name):
    # your code here
    if name == "":
        return None
    elif isinstance(name,str):
        return "hello "+ name + "!"
    else:
        return None
