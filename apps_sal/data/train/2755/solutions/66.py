def multiple_of_index(arr: list) -> list:
    return [
        val
        for idx, val in enumerate(arr)
        if len(arr) > 1 and idx != 0
        if val % idx == 0
    ]
