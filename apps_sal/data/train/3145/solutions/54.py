def greet(name: str) -> str:
    """
    takes a string name and returns a greeting
    """
    if type(name) is str:
        return f"Hello, {name} how are you doing today?"
    else:
        print(f"{name} is not a string")
