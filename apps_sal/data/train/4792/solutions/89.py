def parse_float(string):
    try:
        f = float(string) if isinstance(string, str) else float("".join(string))
        return f
    except ValueError:
        return None
