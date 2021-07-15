def most_common(s: str) -> str:
    return "".join(sorted(s, key = s.count, reverse = True))
