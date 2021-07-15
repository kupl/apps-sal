def calculate_ratio(w, h):
    if not h or not w:
        raise ValueError("Width and height should be > 0")
    for i in range(2, min(w, h) + 1):
        while h % i == w % i == 0:
            h //= i
            w //= i
    return f"{w}:{h}"
