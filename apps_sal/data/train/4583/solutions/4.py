L_LEGS = ['', '^', '/\\', '/╲', '╱╲']
R_LEGS = ['', '^', '/\\', '╱\\', '╱╲']


def draw_spider(legs, body, mouth, eye):
    eyes = eye * (1 << body - 1)
    return f"{L_LEGS[legs]}{'(' * body}{eyes}{mouth}{eyes}{')' * body}{R_LEGS[legs]}"
