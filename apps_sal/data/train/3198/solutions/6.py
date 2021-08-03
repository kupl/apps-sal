def check_exam(answers, solutions):
    return max(sum([0, -1, 4][(ans == sol) + (sol != '')] for ans, sol in zip(answers, solutions)), 0)
