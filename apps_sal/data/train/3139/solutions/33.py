def index(array: list, n: int) -> int:
    return array[n] ** n if n < len(array) else -1
