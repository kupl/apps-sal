def calculate_string(st: str) -> str:
    return f"{eval(''.join((s for s in st if s in '0123456789.+-/*'))):.0f}"
