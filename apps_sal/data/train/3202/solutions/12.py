def greet(name: str, owner: str) -> str:
    """ Get personalized greeting based on passed `name` and `owner`. """
    return f"Hello {('boss' if name == owner else 'guest')}"
