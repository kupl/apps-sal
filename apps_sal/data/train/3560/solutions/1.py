def ski_jump(mountain):
    x = len(mountain)**2 * 1.35
    y = {      x < 10: "He's crap",
         10 <= x < 25: "He's ok",
         25 <= x < 50: "He's flying",
         50 <= x     : "Gold!"}[True]
    return f"{x:.2f} metres: {y}!"
