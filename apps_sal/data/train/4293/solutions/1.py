def calculate_1RM(w, r):
    return (
        w if r == 1 else
        0 if r == 0 else
        round(max(
            w * (1 + r/30),
            100 * w / (101.3 - 2.67123*r),
            w * r**0.10,
        ))
    )
