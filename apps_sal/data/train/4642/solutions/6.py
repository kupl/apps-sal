def calculate_damage(your_type, opponent_type, attack, defense):
    effectivnes_matrix = [[0.5, 0.5, 2, 1], [2, 0.5, 0.5, 0.5], [0.5, 2, 0.5, 1], [1, 2, 1, 0.5]]
    types = ['fire', 'water', 'grass', 'electric']
    effectivness = effectivnes_matrix[types.index(your_type)][types.index(opponent_type)]

    return 50 * (attack / defense) * effectivness
