def ski_jump(mountain):
    distance = len(mountain) ** 2 * 1.35
    if distance <= 10:
        return f"{distance:.2f} metres: He's crap!"
    if distance <= 25:
        return f"{distance:.2f} metres: He's ok!"
    if distance <= 50:
        return f"{distance:.2f} metres: He's flying!"
    if distance > 50:
        return f'{distance:.2f} metres: Gold!!'
