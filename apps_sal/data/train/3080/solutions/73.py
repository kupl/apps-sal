def who_is_paying(name: str) -> list:
    return name[:2].split(" ") if len(name) <= 2 else name.split() + [name[:2]]
