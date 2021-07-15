def color_probability(color, texture):
    return {
        ("smooth", "red"):    "0.33",  # 1:3
        ("bumpy",  "red"):    "0.57",  # 4:7
        ("smooth", "yellow"): "0.33",  # 1:3
        ("bumpy",  "yellow"): "0.28",  # 2:7
        ("smooth", "green"):  "0.33",  # 1:3
        ("bumpy",  "green"):  "0.14"   # 1:7
        }[texture, color]
