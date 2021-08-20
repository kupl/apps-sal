def parse_float(str):
    try:
        return float(str)
    except (TypeError, ValueError):
        return
