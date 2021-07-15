def shoot(results):
    score = sum(rnd[f"P{i+1}"].count("X") * (mul + 1) * (-1)**i for i in (0, 1) for rnd, mul in results)
    return "Pete Wins!" if score > 0 else "Phil Wins!" if score < 0 else "Draw!"

