def calculate_damage(your_type, opponent_type, attack, defense):
    types = {'fire': 0, 'water': 1, 'grass': 2, 'electric': 3}
    effectiveness = [[0.5, 0.5, 2.0, 1.0], [2.0, 0.5, 0.5, 0.5], [0.5, 2.0, 0.5, 1.0], [1.0, 2.0, 1.0, 0.5]]
    return 50 * (attack / defense) * effectiveness[types[your_type]][types[opponent_type]]
