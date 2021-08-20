def lowercase_count(strng: str) -> int:
    """Returns count of lowercase characters."""
    return sum((c.islower() for c in strng))
