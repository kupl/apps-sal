def greet(name, owner):
    return f"Hello {['guest', 'boss'][name == owner]}"
