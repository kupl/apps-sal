import numpy as np

# legs: 2x + 4y + 4z = n(legs)
# heads: x + y + z = n(heads)
# horns: 2z = n(horns)
# where x, y, z: chickens, rabbits, cows
coefficients = np.array([[2, 4, 4], [1, 1, 1], [0, 0, 2]])

def get_animals_count(legs_number, heads_number, horns_number):
    dependents = np.array([legs_number, heads_number, horns_number])
    res = np.linalg.solve(coefficients, dependents)
    return dict(zip(["chickens", "rabbits", "cows"], (int(i) for i in res)))
