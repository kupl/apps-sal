def bool_to_word(boolean: bool) -> str:
    return {True: "Yes", False: "No"}.get(boolean)
