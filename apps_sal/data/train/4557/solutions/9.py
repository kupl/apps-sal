def row_weights(array):
    """Calculate team 1 weights and team 2 weights
    separately, then return."""
    team_1 = sum([array[x] for x in range(len(array)) if x % 2 == 0])
    team_2 = sum([array[x] for x in range(len(array)) if x % 2 != 0])
    return (team_1, team_2)
