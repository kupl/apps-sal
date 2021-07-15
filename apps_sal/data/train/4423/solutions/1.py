def ball_probability(balls):
    colors, (first, second), replaced = balls
    first_choice = colors.count(first) / len(colors)
    second_choice = colors.count(second) / len(colors) if replaced else (colors.count(second) - 1 * (first == second)) / (len(colors) - 1)
    return round(first_choice * second_choice, 3)
