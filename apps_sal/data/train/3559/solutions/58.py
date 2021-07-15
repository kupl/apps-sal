def chromosome_check(sperm):
    sex = 'son' if sperm[1] == 'Y' else 'daughter'
    return f"Congratulations! You're going to have a {sex}."
