def correct(string: str) -> str:
    """It corrects the errors in the digitised text."""
    return string.replace("5", "S").replace("0", "O").replace("1", "I")
