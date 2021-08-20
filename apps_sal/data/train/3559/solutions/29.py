def chromosome_check(sperm):
    gender = 'son' if sperm[-1] == 'Y' else 'daughter'
    return f"Congratulations! You're going to have a {gender}."
