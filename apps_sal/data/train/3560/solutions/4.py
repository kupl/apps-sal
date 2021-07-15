def ski_jump(mountain):
    l = len(mountain)**2 * 1.35
    comment = "Gold!" if 50 < l else f"He's {'crap' if l < 10 else 'ok' if l < 25 else 'flying'}"
    return f"{l:.2f} metres: {comment}!"
