def greet(name=None):
    string_greeting = f"Hello, {name} how are you doing today?"
        
    if type(name) is str:
        return string_greeting
    else:
        return "Name must be a string."
