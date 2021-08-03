def draw_spider(leg, body, mouth, eye):
    legs = ["^ ^", "/\\ /\\", "/╲ ╱\\", "╱╲ ╱╲"][leg - 1].split()
    return legs[0] + "(" * body + eye * 2**(body - 1) + mouth + eye * 2**(body - 1) + ")" * body + legs[1]
