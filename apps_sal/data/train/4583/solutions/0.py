def draw_spider(leg_size, body_size, mouth, eye):
    lleg = ['', '^', '/\\', '/╲', '╱╲'][leg_size]
    rleg = ['', '^', '/\\', '╱\\', '╱╲'][leg_size]
    lbody = '(' * body_size
    rbody = ')' * body_size
    eye *= 2 ** (body_size - 1)
    return f'{lleg}{lbody}{eye}{mouth}{eye}{rbody}{rleg}'
