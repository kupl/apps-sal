def repeat_it(string: str, n: int) -> str:
    return string * n if isinstance(string, str) else 'Not a string'
