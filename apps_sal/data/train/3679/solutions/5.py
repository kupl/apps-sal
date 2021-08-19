def calculate_string(stg):
    return f"{eval(''.join((c for c in stg if c.isdecimal() or c in '.+-*/'))):.0f}"
