def draw_spider(leg_size, body_size, mouth, eye):
    LEG = {1: ['^', '^'], 2: ['/\\', '/\\'], 3: ['/╲', '╱\\'], 4: ['╱╲', '╱╲']}
    left_legs = LEG[leg_size][0]
    right_legs = LEG[leg_size][1]
    left_body = '(' * body_size
    right_body = ')' * body_size
    eyes = eye * 2 ** (body_size - 1)
    return ''.join([left_legs, left_body, eyes, mouth, eyes, right_body, right_legs])
