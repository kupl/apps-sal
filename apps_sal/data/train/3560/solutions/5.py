def ski_jump(mountain):
    length = round(1.35 * len(mountain) ** 2, 2)
    text = ("He's crap", "He's ok", "He's flying", "Gold!")[(length >= 10) + (length >= 25) + (length > 50)]
    return f'{length:.2f} metres: {text}!'
