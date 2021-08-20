L = {1: '^', 2: '/\\', 3: '/╲', 4: '╱╲'}
R = {1: '^', 2: '/\\', 3: '╱\\', 4: '╱╲'}


def draw_spider(leg, body, mouth, eye):
    return L[leg] + '(' * body + eye * (2 ** body // 2) + mouth + eye * (2 ** body // 2) + ')' * body + R[leg]
