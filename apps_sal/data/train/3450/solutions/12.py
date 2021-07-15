def array(string: str) -> str:
    array = string.split(",")
    if len(array) > 2:
        return " ".join(array[1:-1])
