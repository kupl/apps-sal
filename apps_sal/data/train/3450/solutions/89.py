def array(string: str) -> str:
    return (
        None if len(string.split(",")[1:-1]) == 0 else " ".join(string.split(",")[1:-1])
    )


