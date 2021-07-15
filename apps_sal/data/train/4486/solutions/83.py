def repeat_it(string: str,n: int) -> str:
    if not isinstance(string, str):
        return 'Not a string'
    return string * n
