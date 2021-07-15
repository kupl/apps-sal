def hello(name=None):
    return "Hello, World!" if name is None or name is '' else (f"Hello, {name.title()}!")
