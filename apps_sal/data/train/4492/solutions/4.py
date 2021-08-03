colors = {1: "red", 2: "green", 4: "blue", 3: "yellow", 5: "magenta", 6: "cyan", 7: "white"}


def hex_color(codes):
    codes = [int(code) for code in codes.split()]
    most = max(codes, default=0)
    return colors[sum(2**i for i, code in enumerate(codes) if code == most)] if most else "black"
