D = {"warrior":(4, 86), "knight":(5, 86), "wanderer":(3, 86), "thief":(5, 86), "bandit":(4, 86),
     "hunter":(4, 86), "sorcerer":(3, 82), "pyromancer":(1, 84), "cleric":(2, 84), "deprived":(6, 88)}

count = lambda x: round(pow(x, 3) * 0.02 + pow(x, 2) * 3.06 + 105.6 * x - 895)

memo = [0, 0, 673, 1363, 2070, 2794, 3535, 4293, 5068, 5861, 6672, 7501]
def need(level):
    while len(memo) <= level: memo.append(memo[-1] + count(len(memo)))
    return memo[level]

def souls(character, build):
    level, stats = D[character]
    goal = level + sum(build) - stats
    return f"Starting as a {character}, level {goal} will require {need(goal) - need(level)} souls."
