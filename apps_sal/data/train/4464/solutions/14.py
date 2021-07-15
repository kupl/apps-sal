def feast(beast: str, dish: str) -> bool:
    """Return true if dish and beast start and end with same letters."""
    return beast[0] == dish[0] and beast[-1] == dish[-1]
