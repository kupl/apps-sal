exoskeletons = ["Ce n'est pas un insecte...", '^%s%s%c%s%s^', '/\\%s%s%c%s%s/\\', '/╲%s%s%c%s%s╱\\', '╱╲%s%s%c%s%s╱╲', "...and it's also not a bug."]


def draw_spider(leg_size, body_size, mouth, eye):
    (left, right) = [eye * (2 ** body_size // 2)] * 2
    return exoskeletons[leg_size] % ('(' * body_size, left, mouth, right, body_size * ')')
