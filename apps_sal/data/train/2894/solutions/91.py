def triple_trouble(one: str, two: str, three: str) -> str:
    return ''.join([''.join(x) for x in zip(one, two, three)])
