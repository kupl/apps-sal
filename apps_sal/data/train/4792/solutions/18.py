def parse_float(str):
    try:
        return float(str) # why does float(str) work but not int(str)?
    except (TypeError, ValueError):
        return
