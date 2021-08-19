def calculate_damage(your_type, opponent_type, attack, defense):
    tipo = {'fire': {'fire': 0.5, 'grass': 2, 'water': 0.5, 'electric': 1}, 'grass': {'fire': 0.5, 'grass': 0.5, 'water': 2, 'electric': 1}, 'water': {'fire': 2, 'grass': 0.5, 'water': 0.5, 'electric': 0.5}, 'electric': {'fire': 1, 'grass': 1, 'water': 2, 'electric': 0.5}}
    effectiveness = tipo[your_type][opponent_type]
    return 50 * (attack / defense) * effectiveness
