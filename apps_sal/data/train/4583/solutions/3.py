def draw_spider(leg_size, body_size, mouth, eye):
    leg = {1: "^", 2: "/\\", 3: "/╲", 4: "╱╲"}
    r_leg = {1: "^", 2: "/\\", 3: "╱\\", 4: "╱╲"}
    body = {1: "(", 2: "((", 3: "((("}
    r_body = {1: ")", 2: "))", 3: ")))"}
    time = body_size + 1 if body_size == 3 else body_size
    spi = leg[leg_size] + body[body_size] + eye * time + mouth + eye * time +\
          r_body[body_size] +r_leg[leg_size]
    return spi

